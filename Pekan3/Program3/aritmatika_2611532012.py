# Buat file dengan nma aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh : angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yagn dimasukkan akan dikonversi menjadi tipe data integer

angka1_2012 = int(input("Input angka 1: "))
angka2_2012 = int(input("Input angka 2: "))

# Penjumlahan
hasil_2012 = angka1_2012 + angka2_2012
print("\n0perator Penjumlahan")
print("Hasil = ", hasil_2012)

# Pengurangan
hasil_2012 = angka1_2012 - angka2_2012
print("\nOperator Pengurangan")
print("Hasil = ", hasil_2012)

# Perkalian 
hasil_2012 = angka1_2012 * angka2_2012
print("\nOperator Perkalian")
print("Hasil = ", hasil_2012)

# Pembagian, Pembagian Bilangan Bulat, dan Sisa Bagi
if angka2_2012 != 0:
    hasil_2012 = angka1_2012 / angka2_2012
    print("\nOperator Pembagian")
    print("Hasil = ", hasil_2012)

    hasil_2012 = angka1_2012 // angka2_2012
    print("\nOperator Pembagian Bulat")
    print("Hasil = ", hasil_2012)

    hasil_2012 = angka1_2012 % angka2_2012
    print("\nOperator Sisa bagi")
    print("Hasil = ", hasil_2012)
else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil_2012 = angka1_2012 ** angka2_2012
print("\nOperator Pangkat")
print("Hasil = ", hasil_2012)