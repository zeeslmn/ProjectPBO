-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Jun 2021 pada 17.40
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dekstop_rental`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` bigint(20) NOT NULL,
  `kode_barang` varchar(20) NOT NULL,
  `tanggal_sewa` varchar(100) NOT NULL,
  `tanggal_kembali` varchar(100) DEFAULT NULL,
  `username_pelanggan` varchar(50) NOT NULL,
  `jaminan_pelanggan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_karyawan`
--

CREATE TABLE `user_karyawan` (
  `username_karyawan` varchar(30) NOT NULL,
  `nama_karyawan` varchar(100) NOT NULL,
  `no_telp_karyawan` varchar(15) NOT NULL,
  `alamat_karyawan` varchar(255) NOT NULL,
  `password_karyawan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user_karyawan`
--

INSERT INTO `user_karyawan` (`username_karyawan`, `nama_karyawan`, `no_telp_karyawan`, `alamat_karyawan`, `password_karyawan`) VALUES
('der', 'derrel', '08123456789', 'Jember Wow', 'der');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_pelanggan`
--

CREATE TABLE `user_pelanggan` (
  `username_pelanggan` varchar(30) NOT NULL,
  `nama_pelanggan` varchar(100) NOT NULL,
  `no_telp_pelanggan` varchar(15) NOT NULL,
  `alamat_pelanggan` varchar(255) NOT NULL,
  `password_pelanggan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user_pelanggan`
--

INSERT INTO `user_pelanggan` (`username_pelanggan`, `nama_pelanggan`, `no_telp_pelanggan`, `alamat_pelanggan`, `password_pelanggan`) VALUES
('zen', 'zen', '081123456789', 'Jember', 'zen');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`);

--
-- Indeks untuk tabel `user_pelanggan`
--
ALTER TABLE `user_pelanggan`
  ADD PRIMARY KEY (`username_pelanggan`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
