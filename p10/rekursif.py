import os
clear = lambda:os.system('clear')
clear()

def faktorial (n):
    if n == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return n / 2 * faktorial(n-1)  
    return n*faktorial(n-1)

# def fibonacci (o=1, n=1):
#     if n == 1 or n == 2:
#         return 1
#     o = 
#     return fib(n-1) + fib(n-2)

def pangkat (n, o):
    if o == 1:
        return n
    elif o == 0:
        return 1
    
    n*=pangkat(n, o-1)
    return n
    
while True: 
    print("""
██████╗ ███████╗██╗  ██╗██╗   ██╗██████╗ ███████╗██╗███████╗
██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗██╔════╝██║██╔════╝
██████╔╝█████╗  █████╔╝ ██║   ██║██████╔╝███████╗██║█████╗  
██╔══██╗██╔══╝  ██╔═██╗ ██║   ██║██╔══██╗╚════██║██║██╔══╝  
██║  ██║███████╗██║  ██╗╚██████╔╝██║  ██║███████║██║██║ 
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝ 

Pilih fungsi:
[1] Fibonacci
[2] Pangkat
[3] Faktorial
[4] Menghitung maksimum dan minimum
        """)
    user = int(input("> "))
    print()

    if user == 1:
        n = int(input("> "))
        print(fib(n))
        print()
        
        user = input("Lagi? y/n \n> ")
        print()
        if user == "y":
            clear()
            continue
        elif user != "y" or user != "n": 
            print("Tidak sesuai!")
            break
        break
    elif user == 2:
        print("Dalam pengembangan")
    elif user == 3:
        n = int(input("> "))
        print(faktorial(n))
        break
    elif user == 4:
        print("Dalam pengembangan")
    else:
        print("Tidak sesuai!")

    