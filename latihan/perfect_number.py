def bilanganSempurna(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total+=i
    return total == n

bilangan = int(input(""))

if bilanganSempurna(bilangan):
    print("YA")
else:
    print("TIDAK")        