import json

FILE = "kamera.json"

try:
    with open(FILE) as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

while True:
    print("\n 1. Tampilkan  2. Tambah  3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        t = PrettyTable(["ID", "Nama", "Kategori", "Harga Sewa", "Stok"])
        for k in data:
            t.add_row([k["id"], k["nama"], k["kategori"], k["harga_sewa"], k["stok"]])
        print(t)
    elif menu == "2":
        try:
            data.append({
                "id": input("ID: ").upper(),
                "nama": input("Nama: "),
                "kategori": input("Kategori: "),
                "harga_sewa": int(input("Harga sewa: ")),
                "stok": int(input("Stok: ")),
            })
            with open(FILE, "w") as f:
                json.dump(data, f, indent=2)
            print("Data tersimpan.")
        except ValueError:
            print("Harga dan stok harus angka.")
    elif menu == "3":
        break
