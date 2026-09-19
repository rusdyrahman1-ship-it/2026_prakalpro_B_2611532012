# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan indetitas 

print("===================================")
print("1. OPERATOR KEANGGOTAAN")
print("===================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2012 = input("Masukkan beberapa angka, pisahkan dengan koma:")

# Mengubah input menjadi list integer
data_2012 = [int(angka.strip()) for angka in input_data_2012.split(",") ]

nilai_dicari_2012 = int(input("Masukkan angka yang ingin dicari:"))

# Operator in
hasil_2012 = nilai_dicari_2012 in data_2012
print("\nOperator keanggotaan IN")
print(nilai_dicari_2012, "in", data_2012, "=", hasil_2012)

# Operator not in
hasil_2012 = nilai_dicari_2012 not in data_2012
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2012, "not in", data_2012, "=", hasil_2012)


print("\n===================================")
print("2. OPERATOR IDENTITAS")
print("===================================")

# Objek1 menggunakan list dari input pengguna
objek1_2012 = data_2012

# Objek2 menggunakan objek yang sama dengan objek 1
objek2_2012 = objek1_2012

# Objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2012 = data_2012.copy()

print("objek1 =", objek1_2012)
print("objek2 =", objek2_2012)
print("objek3 =", objek3_2012)

# Operator is
hasil_2012 = objek1_2012 is objek2_2012
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_2012)

# Operator is not
hasil_2012 = objek1_2012 is not objek3_2012
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2012)

# Membandingkan identitas dan nilai 
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2012 is objek3_2012)
print("objek1 == objek3 =", objek1_2012 == objek3_2012)