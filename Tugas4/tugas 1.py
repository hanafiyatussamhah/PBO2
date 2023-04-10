print('Hanafiyatussamhah\n210511012\nT121A(R1)\n')

class Film:
    def __init__(self,judul,genre,tahun):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun

class Pencipta:
    def __init__(self,nama,film):
        self.nama = nama
        self.film = film

    def daftar_film(self):
        print(f'\nPencipta\t: {self.nama}\n')
        for film in self.film:
            print(f'Judul\t\t: ',film.judul)
            print(f'Genre\t\t: {film.genre}')
            print(f'Tahun\t\t: {film.tahun}')

film1 = Film('bumi manusia', 'action', 2019)
film2 = Film('perahu krtas', 'romance', 2020)
pencipta1 = Pencipta('manoj punjabi', [film1, film2])
film3 = Film('sbismillah kunikahi suamimu', 'romance', 2021)
film4 = Film('KKN di desa penari', 'horor', 2020)
peneliti2 = Pencipta('manoj punjabi', [film3, film4])
pencipta1.daftar_film()
print('='*40)
peneliti2.daftar_film()
