class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "Mengaum")
class Singa(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Rawr!")
SingaA = Singa("Singa", 2, "Persia")
SingaA.bergerak() # output: Singa bergerak
SingaA.bersuara() # output: Meow!