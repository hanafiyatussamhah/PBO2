class Mahasiswa:
    def __init__(self, nama, umur, nim):
        self.nama = nama
        self.umur = umur
        self.nim = nim
data = Mahasiswa("hana", 20, 210511012,)
try:
    print(data.alamat)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")