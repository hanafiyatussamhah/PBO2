class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")
class Dokter(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang memeriksa.")
dokterA = Dokter("DR.Putrii", 35, "123456")
dokterA.berbicara() # Output: Budi sedang berbicara.
dokterA.mengajar() # Output: Budi dengan NIP 123456 sedang memeriksa.