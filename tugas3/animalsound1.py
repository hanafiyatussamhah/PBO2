from playsound import playsound

class hewan:
    def __init__(self,hewan):
        self.hewan = hewan
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')

class anakkambing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_anakkambing.mp3")

class anjing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_anjing.mp3")

class ayamjago(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_ayamjago.mp3")

class babi(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_babi.mp3")

class bebek(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_bebek.mp3")

class burunghantu(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_burunghantu.mp3")

class gajah(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_gajah.mp3")

class kambing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_kambing.mp3")

class kucing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_kucing.mp3")

class macan(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\Users\lenovo\Documents\PBO SMSTR 4\pertemuan3 PBO2\praktikum\Tugas3\soundanimal_macan.mp3")

def hewan_bersuara(hewan):
    hewan.bersuara()

hewan0 = hewan('Hewan')
hewan1 = anakkambing('Anakkambing')
hewan2 = anjing('Anjing')
hewan3 = ayamjago('Ayamjago')
hewan4 = babi('Babi')
hewan5 = bebek('Bebek')
hewan6 = burunghantu('Burunghantu')
hewan7 = gajah('Gajah')
hewan8 = kambing('Kambing')
hewan9 = kucing('Kucing')
hewan10 = macan('Macan')

hewan_bersuara(hewan0)
hewan_bersuara(hewan1)
hewan_bersuara(hewan2)
hewan_bersuara(hewan3)
hewan_bersuara(hewan4)
hewan_bersuara(hewan5)
hewan_bersuara(hewan6)
hewan_bersuara(hewan7)
hewan_bersuara(hewan8)
hewan_bersuara(hewan9)
hewan_bersuara(hewan10)