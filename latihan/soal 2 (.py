surprise = ["Groucho", "Chico", "Harpo"]

surprise[-1]= surprise[-1].lower()
print(f"huruf kecilkan elemen terakhir: {surprise}")

surprise[-1] = surprise[-1][::-1]
print(f"balikkan huruf elemen terakhir: {surprise}")

surprise[-1] = surprise[-1].upper()
print(f"huruf besarkan elemen terakhir: {surprise}")
