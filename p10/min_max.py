import os 
clear = lambda:os.system('clear')
clear()

def max(list):
    if len(list) == 1:
        return list[0]
    else:
        first = list[0]
        sisa = max(list[1:])
        return first if first > sisa else sisa
    
def min(list):
    if len(list) == 1:
        return list[0]
    else:
        first = list[0]
        sisa = min(list[1:])
        return first if first < sisa else sisa
    



print("""
███╗   ███╗██╗███╗   ██╗    ███╗   ███╗ █████╗ ██╗  ██╗
████╗ ████║██║████╗  ██║    ████╗ ████║██╔══██╗╚██╗██╔╝
██╔████╔██║██║██╔██╗ ██║    ██╔████╔██║███████║ ╚███╔╝ 
██║╚██╔╝██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══██║ ██╔██╗ 
██║ ╚═╝ ██║██║██║ ╚████║    ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
     """)

print("Masukkan list angka (format: 0,1,2,3)")
a, b, c, d = input("> ").split(',')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

list = [a, b, c, d]

print(list)
print("Bilangan tertinggi adalah:", max(list))
print("Bilangan terendah adalah:", min(list))