# 📷 Sistem Manajemen Rental Kamera & Alat Fotografi (CLI)

> **Project Akhir (PA) Dasar-Dasar Pemrograman Python 2026**  
> *Target Konsultasi 1 (Progres Minimal 45% - Selesai 50%)*

Aplikasi manajemen rental kamera berbasis *Command Line Interface* (CLI) yang dibangun secara modular dalam bahasa pemrograman Python. Sistem ini mendukung *multi-role* (Admin & User), autentikasi aman dengan batas login 3 kali (*lockout system*), pembersih layar otomatis berbasis OS, CRUD penuh inventaris kamera, serta penyimpanan data dinamis berbasis file JSON.

---

## 👥 Anggota Kelompok & Pembagian Tugas GitHub

| Nama Anggota | NIM | Username GitHub | Role & Modul Tanggung Jawab |
| :--- | :--- | :--- | :--- |
| **M. Fairuz Firerza Aliushami** | [2609116062] | `@itsraizhu` | **Core Systems & Auth Lead** (`auth.py`, `users.json`) |
| **Muhammad Fachri Razabi** | [2609116069] | `@Fachri2207` | **Admin & CRUD Management Lead** (`kamera.py`, `kamera.json`) |
| **Raisha Achdi Febiandika** | [2609116071] | `@FEBIANDIKA1107` | **User & Main Navigation Lead** (`main.py`, `transaksi.json`) |
| **Alya Shofa** | [2609116077] | `@alyashofaaa15-cloud` | **Laporan** |

---

## 🚀 Fitur yang Selesai (Progres 50% - Konsultasi 1)

### 🔑 1. Autentikasi & Keamanan (`auth.py`)
- [x] **Multi-Role Login**: Membedakan hak akses antara **Admin** dan **User**.
- [x] **Keamanan Password**: Menggunakan library `pwinput` untuk menyembunyikan karakter password.
- [x] **Lockout System**: Batas percobaan login maksimal 3 kali jika password salah.
- [x] **Registrasi User Baru**: Validasi username tidak boleh duplikat (*case-insensitive*) dan panjang minimal 4 karakter.

### 📷 2. Manajemen Inventaris Kamera / CRUD (`kamera.py`)
- [x] **Create**: Menambahkan data kamera/alat fotografi baru (ID, Nama, Kategori, Harga Sewa, Stok) dengan validasi input angka > 0.
- [x] **Read**: Menampilkan katalog/tabel inventaris yang rapi menggunakan `PrettyTable`.
- [x] **Update**: Memperbarui detail harga sewa dan stok kamera.
- [x] **Delete**: Menghapus data kamera dari sistem dengan konfirmasi keamanan (`y/n`).

### 🛠️ 3. Navigasi & Utilitas (`main.py` & `utils.py`)
- [x] **Pembersih Layar OS**: Fungsi `clear_screen()` yang mengenali OS secara otomatis (`cls` untuk Windows, `clear` untuk Linux/Mac).
- [x] **Robust Error Handling**: Penggunaan `try-except` (`ValueError`, `FileNotFoundError`, `JSONDecodeError`) agar program tidak pernah *crash*.
- [x] **Penyimpanan Dinamis JSON**: Otomatis membaca dan menyimpan perubahan data pada file `users.json`, `kamera.json`, dan `transaksi.json`.

---

## 📁 Struktur Repositori Project

```text
SistemRentalKamera/
  data/
  ├── users.json             
  ├── kamera.json             
  └── transaksi.json        
├── README.md              
├── main.py        
├── auth.py                
├── kamera.py            
└── utils.py              
```

---

## 💻 Akun Pengujian (Default Test Accounts)

| Role | Username | Password | Keterangan |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin` | `admin123` | Akses penuh CRUD data kamera |
| **User** | `user1` | `user1234` | Akses katalog & menu peminjaman |

---

Lisensi & Tugas
Proyek ini dibuat untuk memenuhi tugas **Project Akhir (PA) Praktikum Dasar-Dasar Pemrograman Python 2026** (Bobot 50% Nilai Akhir).
