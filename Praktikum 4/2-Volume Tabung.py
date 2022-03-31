# Nama  : Muhammad Ramadhan Muna
# NIM   : 20051397059
# Kelas : 2020 A - D4 Manajemen Informatika

class hasil:
    def hitung(angka):
        print(' ')
        print('-----HASIL-----')
        print('Jari-jari Lingkaran : ', angka.bil1)
        print('Tinggi tabung : ', angka.bil2)
        print('Volume Tabung Adalah :', (22/7*angka.bil1*angka.bil1*angka.bil2))


class nilai(hasil):
    def __init__(self):
        self.bil1 = int(input('Masukan Jari-jari Lingkaran : '))
        self.bil2 = int(input('Masukan Tinggi tabung : '))


coba = ('y')
while coba == ('y') or coba == ('Y'):
    print('Mencari Volume Tabung')

    objek = nilai()
    objek.hitung()
    print(' ')
    break
