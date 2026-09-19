# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakir contoh : a1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2012 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_2012 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_2012)
print("\nA2 =", a2_2012)   

# Konjungsi: bernilai True jika keduanya True
hasil_2012 = a1_2012 and a2_2012
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_2012)

# Disjungsi: bernilai true jika salah satunya True
hasil_2012 = a1_2012 or a2_2012
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_2012)

# Negasi A1: Membalikkan nilai A1
hasil_2012 = not a1_2012
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_2012)

# Negasi A2: Memabalikkan nilai A2
hasil_2012 =  not a2_2012
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_2012)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2012 = a1_2012 != a2_2012
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_2012)