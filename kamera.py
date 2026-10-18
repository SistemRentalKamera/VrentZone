import time
from prettytable import PrettyTable
from utils import clear_screen, load_json, save_json

FILE_KAMERA = 'data/kamera.json'

def tampilkan_kamera():
    kamera_list = load_json(FILE_KAMERA)
    if not kamera_list:
        print("\n[!] Belum ada data kamera/alat fotografi.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Kamera / Alat", "Kategori", "Harga Sewa / Hari", "Stok"]
    
    for k in kamera_list:
        tabel.add_row([k['id'], k['nama'], k['kategori'], f"Rp {k['harga_sewa']:,}", k['stok']])
    
    print(tabel)

def tambah_kamera():
    clear_screen()
    print("----------------------------------------")
    print("        TAMBAH DATA KAMERA BARU         ")
    print("----------------------------------------")
    kamera_list = load_json(FILE_KAMERA)
    
    try:
        id_kamera = input("ID Alat (contoh CAM04): ").upper()
        if not id_kamera:
            print("\n[!] ID Alat tidak boleh kosong!")
            time.sleep(1.5)
            return

        for k in kamera_list:
            if k['id'] == id_kamera:
                print("\n[!] ID Alat sudah ada! Gunakan ID lain.")
                time.sleep(1.5)
                return
                
        nama = input("Nama Alat/Kamera: ")
        if not nama:
            print("\n[!] Nama Alat tidak boleh kosong!")
            time.sleep(1.5)
            return

        kategori = input("Kategori (Mirrorless/DSLR/Lensa/Aksesoris/Stabilizer): ")
        harga_sewa = int(input("Harga Sewa per Hari (Rp): "))
        stok = int(input("Jumlah Stok Awal: "))
        
        if harga_sewa <= 0 or stok < 0:
            print("\n[!] Harga sewa harus > 0 dan stok tidak boleh negatif!")
            time.sleep(1.5)
            return

        kamera_baru = {
            "id": id_kamera,
            "nama": nama,
            "kategori": kategori,
            "harga_sewa": harga_sewa,
            "stok": stok
        }
        kamera_list.append(kamera_baru)
        if save_json(FILE_KAMERA, kamera_list):
            print("\n[✓] Data kamera berhasil ditambahkan!")
        else:
            print("\n[!] Gagal menyimpan data kamera baru.")
    except ValueError:
        print("\n[!] Error: Input harga sewa dan stok harus berupa angka!")
    
    time.sleep(1.5)

def ubah_kamera():
    clear_screen()
    print("----------------------------------------")
    print("         UBAH DATA KAMERA / ALAT        ")
    print("----------------------------------------")
    tampilkan_kamera()
    kamera_list = load_json(FILE_KAMERA)
    
    if not kamera_list:
        time.sleep(1.5)
        return

    id_target = input("\nMasukkan ID Alat yang ingin diubah: ").upper()
    index_found = -1
    for i, k in enumerate(kamera_list):
        if k['id'] == id_target:
            index_found = i
            break

    if index_found == -1:
        print("\n[!] ID Alat tidak ditemukan!")
        time.sleep(1.5)
        return

    item = kamera_list[index_found]
    print(f"\n[Mengubah Data untuk: {item['nama']}]")
    print("(Tekan Enter jika tidak ingin mengubah nilai tertentu)")
    
    nama_baru = input(f"Nama Baru [{item['nama']}]: ")
    kategori_baru = input(f"Kategori Baru [{item['kategori']}]: ")
    harga_str = input(f"Harga Sewa Baru [{item['harga_sewa']}]: ")
    stok_str = input(f"Stok Baru [{item['stok']}]: ")

    try:
        if nama_baru:
            item['nama'] = nama_baru
        if kategori_baru:
            item['kategori'] = kategori_baru
        if harga_str:
            harga_val = int(harga_str)
            if harga_val <= 0:
                print("\n[!] Harga sewa harus > 0!")
                time.sleep(1.5)
                return
            item['harga_sewa'] = harga_val
        if stok_str:
            stok_val = int(stok_str)
            if stok_val < 0:
                print("\n[!] Stok tidak boleh negatif!")
                time.sleep(1.5)
                return
            item['stok'] = stok_val

        kamera_list[index_found] = item
        if save_json(FILE_KAMERA, kamera_list):
            print("\n[✓] Data kamera berhasil diperbarui!")
        else:
            print("\n[!] Gagal memperbarui data.")
    except ValueError:
        print("\n[!] Error: Harga sewa dan stok harus berupa angka!")
    
    time.sleep(1.5)

def hapus_kamera():
    clear_screen()
    print("----------------------------------------")
    print("         HAPUS DATA KAMERA / ALAT       ")
    print("----------------------------------------")
    tampilkan_kamera()
    kamera_list = load_json(FILE_KAMERA)
    
    if not kamera_list:
        time.sleep(1.5)
        return

    id_target = input("\nMasukkan ID Alat yang ingin dihapus: ").upper()
    index_found = -1
    for i, k in enumerate(kamera_list):
        if k['id'] == id_target:
            index_found = i
            break

    if index_found != -1:
        item = kamera_list[index_found]
        konfirm = input(f"Apakah Anda yakin ingin menghapus '{item['nama']}'? (y/n): ").lower()
        if konfirm == 'y':
            del kamera_list[index_found]
            if save_json(FILE_KAMERA, kamera_list):
                print("\n[✓] Data kamera berhasil dihapus.")
            else:
                print("\n[!] Gagal menghapus data.")
        else:
            print("\n[-] Penghapusan dibatalkan.")
    else:
        print("\n[!] ID Alat tidak ditemukan!")
    time.sleep(1.5)
