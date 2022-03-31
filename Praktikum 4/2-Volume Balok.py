# Nama  : Muhammad Ramadhan Muna
# NIM   : 20051397059
# Kelas : 2020 A - D4 Manajemen Informatika

class hasil:
    def hitung(angka):
        print(' ')
        print('-----HASIL-----')
        print('Panjang : ', angka.bil1)
        print('Lebar : ', angka.bil2)
        print('Tinggi  : ', angka.bil3)
        print('Volume Balok Adalah :', (angka.bil1*angka.bil2*angka.bil3))


class nilai(hasil):
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang : '))
        self.bil2 = int(input('Masukan Lebar : '))
        self.bil3 = int(input('Masukan Tinggi : '))


coba = ('y')
while coba == ('y') or coba == ('Y'):
    print('Mencari Volume Balok')

    objek = nilai()
    objek.hitung()
    print(' ')
    break
