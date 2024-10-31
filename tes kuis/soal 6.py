import random

angka_random = random.randint(1, 10)
status = 0
kesempatan = 3

angka = ['1','2','3']

rando = angka[?]
print(rando)

print("================================================================================")
print("KAMI PUNYA ANGKA RAHASIA, AYO TEBAK!")
print("================================================================================")

while status == 0 and kesempatan != 0:
    user = int(input("Masukkan angka: "))
    if user == angka_random:
        print("KAMU BENAR!")
        status = 1
        break
    else:
        if user > angka_random:
            print("Angka terlalu besar \n")
        else:
            print("Angka terlalu kecil \n")
        kesempatan-=1

if kesempatan == 0:
    print("KESEMPATAN HABIS! :(")