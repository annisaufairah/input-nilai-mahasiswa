
print("  PROGRAM PENGELOLAAN STOK TOKO")


# Input data barang
nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan stok awal: "))

# Perulangan transaksi
while True:
    print("===== MENU TRANSAKSI =====")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")

    pilihan = input("Pilih transaksi (1/2/3): ")

    if pilihan == "1":
        jumlah = int(input("Jumlah barang masuk: "))
        stok = stok + jumlah
        print("Barang berhasil ditambahkan!")
        print("Stok sekarang:", stok)

    elif pilihan == "2":
        jumlah = int(input("Jumlah barang keluar: "))

        if jumlah <= stok:
            stok = stok - jumlah
            print("Barang berhasil dikeluarkan!")
            print("Stok sekarang:", stok)
        else:
            print("Stok Tidak Mencukupi!")

    elif pilihan == "3":
        print("\nTransaksi selesai.")
        break

    else:
        print("Pilihan tidak valid!")

# Menampilkan hasil akhir
print("================================")
print("      HASIL AKHIR STOK")
print("================================")
print("Nama Barang :", nama_barang)
print("Stok Akhir  :", stok)
print("================================")