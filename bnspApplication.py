import pyodbc
import pandas as pd
from datetime import datetime

#fungsi untuk membuat koneksi dengan database
def connect_to_database(server, port, database, username, password):
    try:
        connection_string = f'DRIVER={{SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'
        connection = pyodbc.connect(connection_string)
        print("Connection successful")
        return connection
    except pyodbc.Error as e:
        print("Error in connection: ", e)
        return None

#fungsi main menu
def display_menu():
    print("\nMenu:")
    print("1. Buat transaksi baru")
    print("2. Lihat menu yang tersedia")
    print("3. Keluar aplikasi")
    choice = input("Masukan pilihan dari 1-3: ")
    return choice

#fungsi untuk menampilkan menu yang tersedia
def produk_tersedia(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT jenis, ukuran, harga_jual, stok FROM stock_table")
    pilihan_produk = cursor.fetchall()

    print(pilihan_produk)

    pilihan_produk_df = pd.DataFrame.from_records(pilihan_produk, columns=['Jenis Produk', 'Ukuran', 'Harga Jual', 'Stok'])
    print("\nAvailable Products:")
    print(pilihan_produk_df)

def history_pembeli(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT nama_pelanggan FROM transaction_table")
    daftar_nama = cursor.fetchall()
    print(daftar_nama)

def transaksi_jaya_jaya_jaya(connection):
    cursor = connection.cursor()

    #memastikan tanggal yang diinput dimulai dari bulan Februari 2026
    tanggal_mulai = datetime(2026, 2, 1)
    while True:
        transaction_date_str = input("Enter transaction date (YYYY-MM-DD): ")
        try:
            tanggal = datetime.strptime(transaction_date_str, "%Y-%m-%d")
            if tanggal < tanggal_mulai:
                print("Data transaksi harus dimulai dari tanggal 1 Februari 2026")
                continue
        except ValueError:
            print("Format tanggal tidak sesuai")
            continue

        nama_pelanggan = input("Masukan nama pelanggan: ")

        #membuat array kosong untuk menyimpan hasil pembelanjaan dalam satu sesi
        hasil_transaksi = []

        while True:
            #melakukan input secara manual oleh pelanggan
            while True:
                jenis = input("Masukan jenis barang yang dibeli: ")
                query_jenis = cursor.execute("SELECT jenis FROM stock_table")
                jenis_produk = query_jenis.fetchall()
                list_produk = [item[0] for item in jenis_produk]

                if (jenis in list_produk):
                    print("Produk ditemukan")
                    break
                else:
                    print("Produk tidak ada!")

            while True:
                ukuran = int(input("Masukan ukuran: "))
                query_ukuran = cursor.execute("select ukuran from stock_table where jenis = ?",jenis)

                list_ukuran = [i[0] for i in query_ukuran.fetchall()]

                if (ukuran in list_ukuran):
                    print("Ukuran ditemukan!")
                    break
                else:
                    print("Ukuran tidak ditemukan!")

            while True:
                jumlah = int(input("Masukan jumlah yang dipesan: "))
                query_jumlah = cursor.execute("select stok from stock_table where jenis = ? AND ukuran = ?",jenis, ukuran)
                list_jumlah = [i[0] for i in query_jumlah.fetchall()]

                if (jumlah <= list_jumlah[0]):
                    print("Stok tersedia!")
                    break
                else:
                    print("Stok tidak tersedia")

            keterangan = input("Masukkan keterangan tambahan (jika ada): ")

            cursor.execute("INSERT INTO transaction_table (tanggal, nama_pelanggan, jenis, ukuran, jumlah, keterangan) VALUES (?, ?, ?, ?, ?, ?)",
                           tanggal,
                           nama_pelanggan,
                           jenis,
                           ukuran,
                           jumlah,
                           keterangan)

            harga_query = "SELECT harga_jual FROM stock_table WHERE jenis = ? AND ukuran = ?"
            cursor.execute(harga_query, jenis, ukuran)
            harga_jual = cursor.fetchone()

            hasil_transaksi.append({
                'Tanggal': tanggal,
                'Nama Pelanggan': nama_pelanggan,
                'Barang dibeli': jenis,
                'Ukuran': ukuran,
                'Jumlah': jumlah,
                'Harga': (int(harga_jual[0])*jumlah) + (int(harga_jual[0])*0.11),
                'Keterangan': keterangan
            })

            connection.commit()

            receipt_df = pd.DataFrame(hasil_transaksi)
            print("\nStruk belanja:")
            print(receipt_df)

            #logika untuk membuat pelanggan dapat melakukan transaksi lebih dari satu kali dalam satu waktu
            more = input("apakah kamu ingin membuat transaksi lain? (iya/tidak): ")
            if more.lower() != 'iya':
                print("Transaksi selesai!")
                connection.close()
            break

def main():

    #melakukan pengaturan koneksi dengan database (dalam kasus ini database yang digunakan adalah MS SQL Server)
    server = 'localhost\\SQLEXPRESS'
    port = '1433'
    database = 'toko_padi_jaya'
    username = 'admin'
    password = 'ccitindustry'

    connection_string = f'DRIVER={{SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'
    connection = pyodbc.connect(connection_string)

    #melakukan testing koneksi terlebih dahulu sebelum memulai aplikasi
    #connection = connect_to_database(server, port, database, username, password)

    #mengkondisikan looping untuk function display_menu()
    while True:
        choice = display_menu()
        if choice == '1':
            transaksi_jaya_jaya_jaya(connection)
        elif choice == '2':
            produk_tersedia(connection)
        elif choice == '3':
            print("Keluar aplikasi.")
            break
        elif choice == '4':
            history_pembeli(connection)
            break
        else:
            print("Pilihan salah. Silakan masukan nilai dari 1 sampai 3!")

#bagian untuk menjalankan main function
main()

#testing
# server = 'localhost\\SQLEXPRESS'
# port = '1433'
# database = 'toko_padi_jaya'
# username = 'admin'
# password = 'ccitindustry'
#
# connect_to_database(server, port, database, username, password)