# Nama  : Muhammad Ramadhan Muna
# NIM   : 20051397059
# Kelas : 2020 A / D4 Manajemen Informatika

abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

kata = input("Masukkan Kata = ")
modulus = ""
kunci = int(input("Masukkan Kunci = "))

for x in range(len(kata)):
    huruf = abjad.index(kata[x])+kunci
    modulus = modulus+abjad[huruf % 26]
for y in ""+modulus:
    print(y)
