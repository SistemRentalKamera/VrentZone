import time
from utils import clear_screen
from auth import registrasi_user, login_user
from kamera import tampilkan_kamera, tambah_kamera, ubah_kamera, hapus_kamera

def menu_admin(user_aktif):
    while True:
        clear_screen()
        print("------------------------------------------")
        print(f"   MENU ADMIN RENTAL KAMERA ({user_aktif['username']})")
        print("------------------------------------------")
        print("1. Lihat Daftar Kamera")
        print("2. Tambah Data Kamera Baru")
        print("3. Ubah Data Kamera")
        print("4. Hapus Data Kamera")
        print("5. Logout")
        print("------------------------------------------")
        pilihan = input("Pilih Menu (1-5) > ")
        
        if pilihan == '1':
            clear_screen()
            print("------------------------------------------")
            print("      DAFTAR KAMERA & ALAT FOTOGRAFI      ")
            print("------------------------------------------")
            tampilkan_kamera()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '2':
            tambah_kamera()
        elif pilihan == '3':
            ubah_kamera()
        elif pilihan == '4':
            hapus_kamera()
        elif pilihan == '5':
            print("\n[✓] Logout berhasil...")
            time.sleep(1)
            break
        else:
            print("\n[!] Pilihan menu tidak valid!")
            time.sleep(1)

def menu_user(user_aktif):
    while True:
        clear_screen()
        print("------------------------------------------")
        print(f"    MENU USER RENTAL KAMERA ({user_aktif['username']})")
        print(f"    Saldo E-Money: Rp {user_aktif.get('saldo', 0):,}")
        print("------------------------------------------")
        print("1. Lihat Katalog Kamera Tersedia")
        print("2. Logout")
        print("------------------------------------------")
        pilihan = input("Pilih Menu (1-2) > ")
        
        if pilihan == '1':
            clear_screen()
            print("------------------------------------------")
            print("      KATALOG KAMERA & ALAT FOTOGRAFI     ")
            print("------------------------------------------")
            tampilkan_kamera()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '2':
            print("\n[✓] Logout berhasil...")
            time.sleep(1)
            break
        else:
            print("\n[!] Pilihan menu tidak valid!")
            time.sleep(1)

def main():
    while True:
        clear_screen()
        print("------------------------------------------")
        print("  SISTEM MANAGEMENT RENTAL KAMERA (CLI)   ")
        print("  Project Akhir Dasar Pemrograman 2026   ")
        print("------------------------------------------")
        print("1. Login Akun")
        print("2. Registrasi User Baru")
        print("3. Keluar Aplikasi")
        print("------------------------------------------")
        pilihan = input("Pilih Menu (1-3) > ")
        
        if pilihan == '1':
            user = login_user()
            if user:
                if user.get('role') == 'admin':
                    menu_admin(user)
                else:
                    menu_user(user)
        elif pilihan == '2':
            registrasi_user()
        elif pilihan == '3':
            print("\n[✓] Terima kasih telah menggunakan Sistem Rental Kamera CLI!")
            break
        else:
            print("\n[!] Pilihan menu tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()
