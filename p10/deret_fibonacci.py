def fib (n=1):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print("""
███████╗██╗██████╗  ██████╗ ███╗   ██╗ █████╗  ██████╗ ██████╗██╗
██╔════╝██║██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝██╔════╝██║
█████╗  ██║██████╔╝██║   ██║██╔██╗ ██║███████║██║     ██║     ██║
██╔══╝  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║██║     ██║     ██║
██║     ██║██████╔╝╚██████╔╝██║ ╚████║██║  ██║╚██████╗╚██████╗██║
╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚═╝

Berapa deret fibonacci yang ingin anda cetak?
      """)

n = int(input("> "))
for i in range(1,n+1):
    print(fib(i), end=" ")


