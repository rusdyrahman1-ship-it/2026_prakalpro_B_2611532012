# Buat file dengan nama file multi_if2_NIM.py
# Buat program untuk kondisional if
# Buat variabel ditambah 4 digit NIM terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program ini Menghitung Diskon Belanja

# Input dari user
total_belanja_2012 = float(input("Masukkan total belanja (Rp): "))

# input status member (mengecek apakah user mengetik 'y' atau 'ya' )
input_member_2012 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_2012 = input_member_2012 in ["y", "ya"]

# input status kode promo (mengecek apakah user mengetik 'y' atau 'ya' )
input_promo_2012 = input("Apakah Kode Promo valid (y/t): ").strip().lower()
kode_promo_valid_2012 = input_promo_2012 in ["y", "ya"]

total_diskon_persen_2012 = 0

# Nilai if terpisah: setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (diakumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2012 > 1000000:
    total_diskon_persen_2012 += 10 #Diskon Belanja Besar

if is_member_2012:
    total_diskon_persen_2012 += 5 #Diskon Member

if kode_promo_valid_2012:
    total_diskon_persen_2012 += 15 #Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2012 = total_belanja_2012 * (total_diskon_persen_2012 / 100)
total_bayar_2012 = total_belanja_2012 - nominal_diskon_2012

# Outputa Hasil
print("\n=== Rincian Pembayaran ===")
print(f"Total Diskon : {total_diskon_persen_2012}% (Rp {nominal_diskon_2012:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_2012:,.0f}")

print(f"Total Diskon yang Anda dapatkan: {total_diskon_persen_2012}% ")
# Output: Total diskon Anda yang Anda Dapatkan: 30% jika Anda belanja 1 juta, member, dan kode promo valid 