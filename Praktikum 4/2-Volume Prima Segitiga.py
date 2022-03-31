# Nama  : Muhammad Ramadhan Muna
# NIM   : 20051397059
# Kelas : 2020 A - D4 Manajemen Informatika

class hasil:
    def hitung(angka):
        print(' ')
        print('-----HASIL-----')
        print('Panjang alas : ', angka.bil1)
        print('Tinggi : ', angka.bil2)
        print('Tinggi Prisma  : ', angka.bil3)
        print('Volume Prisma Segitiga Adalah :',
              (1/2*angka.bil1*angka.bil2)*angka.bil3)


class nilai(hasil):
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang alas : '))
        self.bil2 = int(input('Masukan Tinggi : '))
        self.bil3 = int(input('Masukan Tinggi Prisma : '))


coba = ('y')
while coba == ('y') or coba == ('Y'):
    print('Mencari Volume Prisma Segitiga')

    objek = nilai()
    objek.hitung()
    print(' ')
    break
