print("Barang apakah yang anda beli? \n 1: Barang baru \n 2: Barang bekas")
tipe_barang = int(input("Pilihan anda:"))
harga_barang = int(input("Masukkan harga barang sebelum diskon (jangan gunakan titik): Rp"))

#1 = baru; 2 = bekas
if tipe_barang == 1:
    harga_barang-=harga_barang * 0.1
else:
    if harga_barang <= 50000:
        harga_barang-= harga_barang * 0.15
    elif harga_barang <= 200000:
        harga_barang -= harga_barang * 0.20
    else:
        harga_barang -= harga_barang * 0.25
        
print(f"Total yang harus anda bayar adalah: Rp{int(harga_barang)} !")