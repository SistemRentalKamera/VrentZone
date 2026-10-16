import json

with open("json/Transaksi.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

    def tambah_data(id, nama, kategori, harga, jumlah):
        data.append({
            "id": id,
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "jumlah": jumlah
        })

        return "Data ditambah"

    def simpan_file():
        with open("json/Transaksi.json", "w", encoding = "utf-8") as f:
            json.dump(data, f, indent = 4)
            return "tersimpan transaksi ke Transaksi"

print("=====data transaksi=====")
print(data)

print ("\n", tambah_data("CAM03", "Fujufilm X-T4 Body", "Kamera Mirrorless", 220000, 2))

print("\n", simpan_file())

print ("===== data setelah ditambah =====")

print(data)
