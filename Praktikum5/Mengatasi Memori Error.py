try:
    Mahasiswa = "hana" * (14**14)
except MemoryError:
    print("Memori tidak cukup untuk menampung data yang diminta!")