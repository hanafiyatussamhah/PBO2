print('hanafiyatussamhah\n210511012\nT121A(R1)\n')

class Penulis:
    def __init__(self,nama):
        self.nama = nama
        self.inventory = Inventory()

    def tampil(self):
        print(f'\nPenulis\t\t: {self.nama}\n')

class Buku:
    def __init__(self,judul,publish,penerbit):
        self.judul = judul
        self.publish = publish
        self.penerbit = penerbit

    def get_judul(self):
        return self.judul
    
    def get_publish(self):
        return self.publish
    
    def get_penerbit(self):
        return self.penerbit
    
class Inventory:
    def __init__(self):
        self.books = []

    def add_buku(self,buku):
        self.books.append(buku)

    def daftar_buku(self):
        for buku in self.books:
            print(f'Judul\t\t: ',buku.judul)
            print(f'Terbit\t\t: ',buku.publish)
            print(f'Penerbit\t: ',buku.penerbit)

penulis1 = Penulis('tereliye')
bulan = Buku('bulan', 'djakarta, 2019', 'graha Pustaka')
matahari = Buku('matahari', 'djakarta, 2019', 'graha Pustaka')
bintang = Buku('bintang', 'Djakarta, 2020', 'graha Pustaka')
sepatu = Buku('sepatu', 'djakarta, 2017', 'graha Pustaka')
penulis1.inventory.add_buku(bulan)
penulis1.inventory.add_buku(matahari)
penulis1.inventory.add_buku(bintang)
penulis1.inventory.add_buku(sepatu)
penulis1.inventory.books
penulis1.tampil()
print('='*20)
penulis1.inventory.daftar_buku()