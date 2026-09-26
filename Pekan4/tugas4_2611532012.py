# Buat file tugas dengan nama file tugas4_NIM.py
# Buat program if, elif, dan else
# Buat variabel ditambah 4 digit NIM terakhir contoh : tiket_1234
# Program ini menggunakan fungsi input()
# Program ini digunakan untuk menghitung sistem loket terpadu dan audit transaksi ekspedisi wahana

# Masukkan data yang digunakan untuk program 
print("\n=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_pengunjung_2012 = input("Masukkan Nama Pengunjung :")
umur_2012 = int(input("Masukkan Umur Anda :"))
sim_2012 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()

# Masukkan nomor tiket berdasarkan wahana yang ada, jumlah tiket, status member, dan promo valid
# Buat program match case untuk menentukan kategori wahana dan harga wahana
print("Pilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50.000)")
print("  2. Arung Jeram          (Rp 75.000)")
print("  3. Motor ATV Ekstrim    (Rp 120.000)")
print("  4. Roller Coaster Kilat (Rp 100.000)")
print("  5. All-Access VIP       (Rp 220.000)")
wahana_2012 = int(input("Masukkan nomor tiket (1-5) : "))
match wahana_2012:
 case 1:
  nama_2012 = "Wahana Safari Rimba" 
  Harga_Satuan_2012 = 50000
 case 2:
  nama_2012 = "Arung Jeram" 
  Harga_Satuan_2012 = 75000
 case 3:
  nama_2012 = "Motor ATV Ekstrim" 
  Harga_Satuan_2012 = 120000
 case 4:
  nama_2012 = "Roller Coaster Kilat" 
  Harga_Satuan_2012 = 100000
 case 5:
  nama_2012 = "All-Acsess VIP" 
  Harga_Satuan_2012 = 220000
 case _:
  print("Paket wahana tidak valid!")
jumlah_tiket_2012 = int(input("Masukkan jumlah tiket :"))
member_2012 = input("Apakah Anda Member (y/t) :").strip().lower()
promo_2012 = input("Apakah Kode Promo Valid :").strip().lower()

# Buat program kelayakan pengendara menggunakan if, elif ,dan else 
# Program ini akan muncul jika wahana yang dipilih adalah 3 (Motor ATV Ekstrim) dan 5 (All- Access VIP)
if wahana_2012 == 3 & 5 :
 print("\n=== KELAYAKAN PENGENDARA WAHANA ===")
 if umur_2012 >= 17 and sim_2012 == 'y':
  status_akses_2012 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri"
 elif umur_2012 >= 17 and sim_2012 != 'y':
  status_akses_2012 = "Anda sudah dewasa tetapi Anda harus didampingi dengan orang yang sudah punya SIM"
 elif umur_2012 < 17 and sim_2012 == 'y':
  status_akses_2012 = "Usia Anda belum cukup untuk memiliki SIM"
 else:
  status_akses_2012 = "Anda belum boleh mengendarai ATV sendiri "
  print(f"Status Akses: {status_akses_2012}")

print("\n=== HASIL VALIDASI ===")
is_member_2012 = member_2012 in ["y", "ya"]
promo_valid_2012 = promo_2012 in ["y", "ya"]
print("Apakah status member aktif : ", is_member_2012)
print("Apakah promo benar valid : ", promo_valid_2012)

print("\n=== HASIL KALKULASI ===")
subtotal_2012 = Harga_Satuan_2012 * jumlah_tiket_2012
total_diskon_2012 = 0
if subtotal_2012 >= 200000: 
 total_diskon_2012 += 10 # Diskon 10% untuk pembelian besar
if is_member_2012:
 total_diskon_2012 += 5 # Diskon 5% untuk member aktif
if promo_valid_2012:
 total_diskon_2012 += 15 # Diskon 15% untuk promo valid
if jumlah_tiket_2012 >= 5:
 total_diskon_2012 += 5 # Diskon 5% untuk jumlah tiket lebih dari 5 tiket

nominal_diskon_2012 = subtotal_2012 * (total_diskon_2012/100)
total_bayar_2012 = subtotal_2012 - nominal_diskon_2012
print(f"Total Diskon : {total_diskon_2012}% (Rp {nominal_diskon_2012:.0f})")
print(f"Total bayar : Rp {total_bayar_2012:.0f}")
# Program untuk mendapatkan Souvenir
if total_bayar_2012 >= 300000:
 print("Selamat! Anda berhak mendapatkan mendapatkan Souvenir")
else:
 print("Terima kasih telah berkunjung") 