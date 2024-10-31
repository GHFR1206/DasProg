things = ['mozarella', 'cinderella', 'salmonella']

things[1] = things[1].upper()

print(f"Huruf besarkan elemen merujuk ke seseorang: {things}")

things[0].upper()
print(f"buatlah elemen 'mozarella' menjadi huruf besar: {things}")

things.pop(-1)
print(f"hilangkan elemen 'salmonella': {things}")
