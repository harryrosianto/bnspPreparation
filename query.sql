-- membuat database terlebih dahulu
CREATE DATABASE toko_padi_jaya;

-- hanya untuk memastikan menggunakan database yang tepat
USE toko_padi_jaya;

-- buat tabel yang menyimpan stok barang
CREATE TABLE stock_table (
    nomor_produk INT PRIMARY KEY IDENTITY(1,1),
    jenis VARCHAR(50),
    ukuran INT,
    harga_jual DECIMAL(10, 2),
    stok INT
);

-- masukan data ke dalam stock_table
INSERT INTO stock_table (jenis, ukuran, harga_jual, stok) VALUES
('Topi Koki Setra Ramos', 5, 73000, 124),
('Rojolele Super', 5, 63000, 76),
('Rojolele Super', 10, 120000, 53),
('Rojolele Super', 25, 300000, 37),
('BMW Setra Ramos', 5, 68000, 89),
('Bunga Ramos Setra', 5, 64000, 147),
('Bunga Ramos Setra', 10, 120000, 32),
('Maknyus Premium', 5, 71000, 154),
('Maknyus Premium', 25, 338000, 99),
('Puregreen Beras Merah', 1, 22000, 64),
('Puregreen Beras Merah', 2, 45000, 39);

-- verifikasi data
SELECT * FROM stock_table;

-- buat tabel transaksi bernama transaction_table
CREATE TABLE transaction_table (
    transaction_number INT PRIMARY KEY IDENTITY(1,1),
    tanggal DATE NOT NULL,
    nama_pelanggan VARCHAR(50) NOT NULL,
    jenis VARCHAR(50),
    ukuran INT,
    jumlah INT CHECK (jumlah > 0),
    keterangan VARCHAR(255)
);

-- verifikasi data dari tabel transaksi
SELECT * FROM stock_table;

-- buat trigger jaga-jaga
CREATE TRIGGER update_stock_after_transaction
ON transaction_table
AFTER INSERT
AS
BEGIN
    UPDATE stock_table
    SET stok = stok - inserted.jumlah
    FROM stock_table
    INNER JOIN inserted
    ON stock_table.jenis = inserted.jenis
    AND stock_table.ukuran = inserted.ukuran
END;

-- Create the stock table
CREATE TABLE stock (
    nomor_produk INT PRIMARY KEY,
    jenis VARCHAR(255),
    ukuran VARCHAR(255),
    harga_jual DECIMAL(10, 2),
    stok INT
);


select * from stock_table
select ukuran from stock_table where jenis = 'Rojolele Super'
select stok from stock_table where jenis = 'Rojolele Super' AND ukuran = 25
