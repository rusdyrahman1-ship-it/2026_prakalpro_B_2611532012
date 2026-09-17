# Buat file dengan nama bitwisse_NIM.py
# Nama variabel ditambah 4 digit terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n===================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_2012 = int(input("Masukkan angka bitwise-1 : "))
angka2_2012 = int(input("Masukkan angka bitwise-2 : "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_2012, "| biner =", bin(angka1_2012))
print("angka2 =",angka2_2012, "| biner =", bin(angka2_2012))

# Bitwise AND 
hasil_2012 = angka1_2012 & angka2_2012
print("\nBitwse AND (&)")
print(angka1_2012, "&", angka2_2012)
print("Biner Hasil =", bin(hasil_2012))
print("Biner hasil (8 bit) =", format(hasil_2012, "08b"))

# Bitwise OR
hasil_2012 = angka1_2012 | angka2_2012
print("\nBitwise OR (|)")
print(angka1_2012, "|", angka2_2012, "=", hasil_2012)
print("Biner hasil =", bin(hasil_2012))
print("Biner hasil (8 bit) =", format(hasil_2012, "08b"))

# Bitwise XOR 
hasil_2012 = angka1_2012 ^ angka2_2012
print("\nBitwise XOR (^)")
print(angka1_2012, "^", angka2_2012, "=", hasil_2012)
print("Biner hasil =", bin(hasil_2012))
print("Biner hasil (8bit) ="), format(hasil_2012, "08b")

#Bitwise NOT 
hasil_2012 = ~angka1_2012
print("\nBitwise NOT (~)")
print("~", angka1_2012, "=", hasil_2012)
print("Biner hasil =", bin(hasil_2012))
print("Biner hasil (8bit) =", format(hasil_2012, "08b"))

# Bitwise geser kiri
jumlah_geser_2012 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2012 = angka1_2012 << jumlah_geser_2012
print("\nBitwise geser kiri (<<)")
print(angka1_2012, "<<", jumlah_geser_2012, "=", hasil_2012)
print("Biner hasil =", bin(hasil_2012))
print("Biner hasil (8bit) =", format(hasil_2012, "08b"))

# Bitwise geser kanan
hasil_2012 = angka1_2012 >> jumlah_geser_2012
print("\nBitwise geser kanan (>>)")
print(angka1_2012, ">>", jumlah_geser_2012, "=", hasil_2012)
print("Biner hasil =", bin(hasil_2012))
print("Biner hasil (8bit) =", format(hasil_2012, "08b"))