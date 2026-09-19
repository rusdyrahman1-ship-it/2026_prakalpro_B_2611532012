# Buat file dengan nama file tugas3_NIM.py
# Program sistem transaksi toko dengan menggunakan operator Python yang telah dipelajari
# Program ini menggunakan fungsi input()
# Menggunakan variabel ditambah 4 digit terakhir contoh : angka_1234

print("\n=== SISTEM TRANSAKSI TOKO ===")
# Memasukkan Data Pelanggan berupa string dan integer
nama_2012 = input("Masukkan Nama Pelanggan :")
status_2012 =input("Masukkan Status Pelanggan (member/non member) :")
total_belanja_2012 = int(input("Masukkan Total Belanja :"))
total_barang_2012 = int(input("Masukkan Total Barang : "))
kode_promo_2012 = input("Masukkan Kode Promo :")
print(" ")
# Cek Validasi (Operator Perbandingan)
print("\n=== HASIL VALIDASI ===")
# Menggunakan Operator perbandingan lebih besar dari atau sama dengan (=)
belanja_cukup_2012 = total_belanja_2012 >= 200000
print("Belanja >= Rp 200000 :", belanja_cukup_2012)
barang_cukup_2012 = total_barang_2012 >= 3
print("Jumlah Barang >= 3 :", barang_cukup_2012)
# Menggunakan operator perbandingan (==) yang mana kata yang diinput tidak diperhatikan huruf kapital. huruf kecil, dan spasi
member_2012 = status_2012.strip().lower() == "member"
print("Status Member :", member_2012)
# Menggunakan operator keanggotaan yang mana kata yang diinput tidak diperhatikan huruf kapital, huruf kecil, dan spasi
daftar_promo_2012 = ("GOHEMAT" ,"HEMAT10" ,"HEMATGO")
promo_tersedia_2012 = kode_promo_2012.strip().upper() in daftar_promo_2012
# Menggunakan Operator logika konjungsi (and)
print("Kode Promo Tersedia :", promo_tersedia_2012)
dapat_diskon_2012 = belanja_cukup_2012 and barang_cukup_2012
print("Mendapatkan Diskon :", dapat_diskon_2012 )
dapat_promo_2012 = member_2012 and promo_tersedia_2012
print("Mendapatkan Promo :", dapat_promo_2012)
print(" ")
# Perhitungan Diskon, Total Pembayaran, dan Rata - Rata Barang menggunakan Operator Aritmatika (perkalian(*) dan pengurangan(-))
print("\n=== HASIL PERHITUNGAN ===")
if dapat_diskon_2012:
    diskon_2012 = 0.03
else:
    diskon_2012 = 0
if dapat_promo_2012:
    promo_2012 = 0.10
else:
    promo_2012 = 0
total_diskon_2012 = total_belanja_2012 * diskon_2012
total_promo_2012 = total_belanja_2012 * promo_2012
total_pembayaran_2012 = total_belanja_2012 - total_diskon_2012 - total_promo_2012
rata2_barang_2012 = total_pembayaran_2012 / total_barang_2012
print("Diskon :", "Rp", int(total_diskon_2012))
print("Promo  :", "Rp", int(total_promo_2012))
print("Total Pembayaran :", "Rp", int(total_pembayaran_2012) )
print("Rata - Rata Harga Barang :", "Rp", int(rata2_barang_2012))
print(" ")
print("\n=== HAK AKSES===")
# Flag Bit untuk kode akses 
free_shipping_2012 = total_pembayaran_2012 >= 200000
Member_2012 = 1 
Diskon_2012 = 2
Free_shipping_2012 = 4
Promo_2012 = 8
# Menentukan nilai kode akses dengan menggunakan operator assignment (|=)
kode_akses_2012 = 0
if member_2012:
   kode_akses_2012 |= Member_2012
if dapat_diskon_2012:
   kode_akses_2012 |= Diskon_2012
if free_shipping_2012:
   kode_akses_2012 |= Free_shipping_2012
if dapat_promo_2012 :
   kode_akses_2012 |= Promo_2012
# Menampilkan kode 4 bit dari kode akses dan juga menampilkan apakah pernyataan tersebut benar atau salah menggunakan tipe data boolean
print("Kode Hak Akses   :", format(kode_akses_2012, "04b"))
print("Member Access    :", bool(kode_akses_2012 & Member_2012))
print("Diskon Access    :", bool(kode_akses_2012 & Diskon_2012))
print("Free Shipping Access :", bool(kode_akses_2012 & Free_shipping_2012))
print("Promo Access     :", bool(kode_akses_2012 & Promo_2012))
print("")
# Cek Referensi Status Membere dengan menggunakan Operator Identitas
print("\n=== Cek Referensi Status Member ===")
referensi_status_2012 = member_2012         
hasil_2012 = referensi_status_2012 is member_2012 
print(" referensi status is member  :", hasil_2012)
 
print("\n=== Cek Objek Kode Akses ===")
kode_akses_lain_2012 = kode_akses_2012      
hasil_2012 = kode_akses_lain_2012 is kode_akses_2012
print("kode akses lain is kode akses :", hasil_2012)
# OPERASI BITWISE dengan bilangan biner format 4 bit serta menampikan bilangan desimal dari bilangan biner tersebut
print("\n=== OPERASI BITWISE===")
print("\n=== Kode Status Transaksi ===")
print(format(Member_2012, "04b"), "|", format(Diskon_2012,"04b"), "|", format(Free_shipping_2012, "04b"), "|", format(Promo_2012,"04b"))
print("Kode Biner   :", format(kode_akses_2012, "04b"))
print("Kode Desimal :", format(kode_akses_2012))
print("")
print("\n=== Pemeriksaan Status ===")
# Cek Member dengan menggunakan Operasi Bitwise (AND(&))
print("Cek member")
print(format(kode_akses_2012,"04b"), "&", format(Member_2012,"04b"))
Hasil_biner_2012 = kode_akses_2012 & Member_2012
print(format(Hasil_biner_2012,"04b"))
print("\nCek Promo")
print(format(kode_akses_2012, "04b"), "&", format(Promo_2012, "04b"))
hasil_biner_2012 = kode_akses_2012 & Promo_2012
print(format(hasil_biner_2012, "04b"))
# Perbandingan Status dengan menggunakan Operasi Bitwise (XOR (^))
print("\n ===Perbandingan Status ===")
kode_referensi_2012 = 0b1011
print("Kode Transaksi :", format(kode_akses_2012, "04b"))
print("Kode Referensi :", format(kode_referensi_2012, "04b"))
hasil_biner_2012 = kode_akses_2012 ^ kode_referensi_2012
print(format(kode_akses_2012 ^ kode_referensi_2012,"04b"))
print("Hasil Biner :", format(hasil_biner_2012,"04b"))
print("Hasil desimal :", hasil_biner_2012)
