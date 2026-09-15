print("=== SISTEM REGISTRASI PRATIKAN ALPRO 2026 === ")
nama_mahasiswa_2012 = "Muhammad Rusdy Rahman"
jenis_kelamin_2012 = "L"
umur_2012 = 18
skor_tes_awal_2012 = 82.5
alamat_2012 ="""
Batu Belah
Kec. Kampar
Kab. Kampar
Prov. Riau """
id_token_sinyal_2012 = 100 + 3j 
batas_minimum_nilai_2012 = 75
status_kelulusan_2012 = skor_tes_awal_2012 >= batas_minimum_nilai_2012
print("Masukkan Nama Mahasiswa : ", nama_mahasiswa_2012)
print("Masukkan Jenis Kelamin : ", jenis_kelamin_2012)
print("Masukkan Umur : ", umur_2012)
print("Masukkan Skor Tes awal : ", skor_tes_awal_2012)

print("=== DATA PRATIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ", nama_mahasiswa_2012 , "|" , "Tipe :", type(nama_mahasiswa_2012))
print("Jenis Kelamin : ", jenis_kelamin_2012, "|" , "Tipe :", type(jenis_kelamin_2012))
print("Alamat Domisili :", alamat_2012,"|", "Tipe :", type(alamat_2012))
print("Umur :", umur_2012,"|", "Tipe :", type(umur_2012))
print("Skor Tes Awal :", skor_tes_awal_2012, "|", "Tipe :", type(skor_tes_awal_2012))
print("ID Token Sinyal :", id_token_sinyal_2012, "|" ,"Tipe :", type(id_token_sinyal_2012))

print("=== STATUS KELULUSAN PRATIKUM ===")
print("Batas Minimum Nilai :", batas_minimum_nilai_2012)
print("Apakah Lulus?:", status_kelulusan_2012, "|", "Tipe: ", type(status_kelulusan_2012))