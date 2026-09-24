# Buat file dengan nama if2_NIM.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit terakhir dari NIM contoh : ipk_1234
# Program ini menggunakan fungsi input()

ipk_2012 = float(input("Input IPK Anda = "))

if ipk_2012 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_2012))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")