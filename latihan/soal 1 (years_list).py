tahun_lahir = int(input("Tahun lahir anda: "))
counter = 5
years_list = []

while counter > 0:
    tahun_lahir+=1
    years_list.append(tahun_lahir)
    counter-=1
    
print(f"{years_list}")
print(f"Tahun berapakah anda umur 3 tahun? {years_list[2]}")
print(f"Tahun berapakah dalam years list anda paling tua? {max(years_list)}")
