# Buat file dengan nama konstanta_2611532012.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import final 
PI_2012: Final= 3.14
print("pi: %f" % (PI_2012))
jari_2012 = float(input('Masukkan nilai jari-jari: '))
luas_2012 = PI_2012 * jari_2012
print("Luas lingkaran dengan jari - jari %.2f adalah %.2f" % (jari_2012, luas_2012))