nama = input("Nama: ")
usia = int(input("Usia: "))
tahun = 2024

while usia != 50:
    tahun+=1
    usia+=1
    
print(f"Nama anda {nama}, anda berusia {usia} tahun. Pada tahun {tahun} anda akan berusia 50 tahun")
    
selisih = 50 - usia
tahun_akhir = tahun + selisih
print(tahun_akhir)
