# Buat file dengan nama Boolean_2012.py
# nama variabel ditambah 4 digit terakhir NIM contoh:nilai_2012
# Deklarasi variabel dengan tipe data Boolean
is_lulus_2012 = True
is_cumlaude_2012 = True

# Menggunakan nilai Boolean dari kondisi 
nilai_2012 = 85
batas_lulus_2012 = 75

# Menentukan nilai dari boolean dari kondisi
status_kelulusan_2012 = nilai_2012 >= batas_lulus_2012 #Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_2012)
print("Apakah Lulus?:", status_kelulusan_2012)
if is_lulus_2012 and is_cumlaude_2012:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")
