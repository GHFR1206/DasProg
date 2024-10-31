harga_pokok = float(input("Masukkan harga pokok: "))
harga_jual = float(input("Masukkan harga jual: "))

persentase = ((harga_jual - harga_pokok) / harga_pokok) * 100 
print(f"Persentase keuntungan: {persentase:.2f}%")