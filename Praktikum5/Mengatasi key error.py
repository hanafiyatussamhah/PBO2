data = {"Kucing": 10, "kelinci": 20, "anjing": 14}
try:
    value = data["Ayam"]
except KeyError:
    print("Key yang dicari tidak ditemukan pada data!")