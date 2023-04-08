print('Hanafiyatussamhah\n210511012\nT121A(R1)\n')

class Jurnal:
    def __init__(self,title,date):
        self.title = title
        self.date = date

class Peneliti:
    def __init__(self,nama,jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t: {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t: ',jurnal.title)
            print(f'Published\t: {jurnal.date}')

jurnal1 = Jurnal('sistem informasi manajemen nilai siswa berbasis web', 2019)
jurnal2 = Jurnal('sistem pakar  mengidentifikasi penanggulangan penyakit pada gigi dan mulut', 2020)
peneliti1 = Peneliti('Dian novianti', [jurnal1, jurnal2])
jurnal3 = Jurnal('sistem pendukung keputusan pemilihan guru terbaik dengan metode simple additive weighting', 2021)
jurnal4 = Jurnal('sistem jaringan  distribusi air bersih', 2020)
peneliti2 = Peneliti('Harry gunawan', [jurnal3, jurnal4])
peneliti1.daftar_jurnal()
print('='*40)
peneliti2.daftar_jurnal()
