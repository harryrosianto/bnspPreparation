### **Instruksi**

1. Baca dan pelajari setiap instruksi di bawah ini dengan cermat sebelum mulai mengerjakan.
2. Ajukan klarifikasi kepada asesor kompetensi jika ada hal yang belum jelas.
3. Lakukan pekerjaan sesuai urutan proses yang telah ditentukan.
4. Seluruh proses kerja harus mengikuti SOP/WI yang berlaku (jika ada).

---

### **Skenario Tugas Praktik Demonstrasi**

Sebuah toko bahan makanan bernama *"Sembako Sejahtera"* menjual beberapa jenis produk dengan data stok sebagai berikut:

| No | Produk               | Berat | Harga Beli | Harga Jual | Stok |
|----|-----------------------|-------|------------|------------|------|
| 1  | Minyak Goreng Sari   | 1 L   | Rp. 20.000 | Rp. 23.000 | 150  |
| 2  | Gula Manis Indah     | 1 kg  | Rp. 13.000 | Rp. 15.000 | 200  |
| 3  | Beras Wangi Setia    | 5 kg  | Rp. 60.000 | Rp. 68.000 | 75   |
| 4  | Tepung Terigu Lestari | 1 kg  | Rp. 8.000  | Rp. 9.500  | 120  |
| 5  | Garam Beryodium      | 500 g | Rp. 3.000  | Rp. 3.500  | 300  |

### Persyaratan Toko:
- Pelanggan dapat membeli lebih dari satu produk dalam setiap transaksi.
- Sistem mencatat transaksi secara sederhana, hanya berdasarkan nama pembeli.
- Setiap transaksi akan mengurangi stok barang, dan jika stok tidak mencukupi, transaksi dibatalkan.
- Setiap transaksi dikenakan pajak sebesar 10%.

### Transaksi Rutin dan Tidak Rutin:
| No | Tanggal           | Nama Pelanggan    | Produk            | Berat | Jumlah | Keterangan         |
|----|--------------------|-------------------|--------------------|-------|--------|--------------------|
| 1  | Setiap awal bulan | Warung Laris      | Beras Wangi Setia | 5 kg  | 5      | Rutin              |
| 2  | Setiap minggu     | Ibu Murni         | Minyak Goreng Sari | 1 L   | 10     | Rutin              |
| 3  | 1 Februari 2026   | Pak Budi          | Gula Manis Indah   | 1 kg  | 15     | Tidak Rutin       |
| 4  | 15 Februari 2026  | Ibu Rina          | Tepung Terigu Lestari | 1 kg | 20    | Tidak Rutin       |
| 5  | 20 Februari 2026  | Bapak Ari         | Garam Beryodium    | 500 g | 50     | Tidak Rutin       |

### **Tugas:**

1. **Perancangan Sistem**
   - Rancang basis data dan perangkat lunak yang sesuai untuk toko *Sembako Sejahtera*, termasuk pemilihan mesin basis data dan bahasa pemrograman.
   - Buat dokumentasi singkat yang menjelaskan rencana basis data dan pemrograman yang akan digunakan.
   - Tentukan fungsi/prosedur/trigger/perpustakaan yang diperlukan.

2. **Implementasi Sistem**
   - Implementasikan basis data untuk menyimpan data stok dan transaksi toko.
   - Buat trigger dan prosedur yang dapat mengatur stok produk secara otomatis.
   - Buat aplikasi untuk:
     - Mencatat transaksi pembelian oleh pelanggan dan menolak transaksi jika stok tidak mencukupi.
     - Menampilkan ringkasan transaksi lengkap beserta tanggal, nama pelanggan, produk, harga, pajak, dan total harga.
     - Menghitung keuntungan toko selama bulan Februari 2026 berdasarkan data transaksi. (opsional)
     - Menampilkan total pajak yang harus disetor selama bulan Februari 2026. (opsional)
   - Gunakan komentar untuk menjelaskan fungsi kode program.
   - Terapkan penanganan kesalahan untuk menghindari bug, dan gunakan paradigma pemrograman yang sesuai (berorientasi objek/prosedural).

3. **Pengujian**
   - Lakukan debugging untuk memastikan tidak ada kesalahan.
   - Buat dokumentasi singkat mengenai program yang telah dibuat.

---

**Durasi Waktu:** 180 menit
