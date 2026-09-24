# Buat file dengan nama file multi_if_NIM.py
# Buat program untuk kondiisional if
# Nama variabel ditambah 4 digit nim terakhir contoh : ipk_1234
# Program ini menggunakan fungsi input()

umur_2012 = int(input("Input Umur Anda: "))
sim_2012 = input("Apakah Anda Sudah Punya SIM C (y/t) : ")[0]

if umur_2012 >= 17 and sim_2012 == 'y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")

if umur_2012 >= 17 and sim_2012 != 'y':
    print("Anda Sudah Dewasa tetapi Belum Boleh Bawa Motor")

if umur_2012 < 17 and sim_2012 == 'y':
    print("Anda Belum Cukup Umur Punya SIM")

if umur_2012 < 17 and sim_2012 != 'y':
    print("Anda Belum Cukup Umur Bawa Motor")

print("Program Selesai")