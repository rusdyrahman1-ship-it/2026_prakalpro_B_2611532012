# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversikan menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2012 = int(input("Input angka-1 ="))
angka2_2012 = int(input("Input angka-2 ="))

# Lebih besar sama dari
hasil_2012 = angka1_2012 > angka2_2012
print("\nOperator lebih besar dari")
print("angka1 > angka2 =", hasil_2012)

# Lebih kecil dari 
hasil_2012 = angka1_2012 < angka2_2012
print("\nOperator lebih kecil dari")
print("angka1 < angka2 =", hasil_2012)

# Lebih besar dari atau sama dengan 
hasil_2012 = angka1_2012 >= angka2_2012
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil_2012)

# Lebih kecil dari atau sama dengan
hasil_2012 = angka1_2012 <= angka2_2012
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil_2012)

# Sama dengan 
hasil_2012 = angka1_2012 == angka2_2012
print("\nOperator sama dengan")
print("angka1 == angka2 =", hasil_2012)

# Tidak sama dengan 
hasil_2012 = angka1_2012 != angka2_2012
print("\nOperator tidak sama dengan")
print("angka1 != angka2 =", hasil_2012)

# Tambahan: Perbandingan berantai dalam Python
hasil_2012 = 0 < angka1_2012 < 100
print("0 < angka1 < 100 =", hasil_2012)

hasil_2012 = 0 < angka2_2012 < 100
print("0 < angka2 < 100 =", hasil_2012)