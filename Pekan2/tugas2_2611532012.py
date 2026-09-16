from typing import final 
batas_lulus_2012: final = 75.0
print("=== SISTEM REGISTRASI PRATIKAN ALPRO 2026 === ")
nama_mahasiswa_2012 = input("Masukkan Nama :")
jenis_kelamin_2012 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_2012 = int(input("Masukkan Umur : "))
skor_tes_awal_2012 =float(input("Masukkan Skor Tes Awal : "))
print( " " )
print("=== DATA PRATIKAN & HASIL PEMERIKSAAN ===")
alamat_2012 ="""
Batu Belah,
Kec. Kampar,
Kab. Kampar,
Prov. Riau """
print("Nama Mahasiswa : ", nama_mahasiswa_2012 , "|" , "Tipe :", type(nama_mahasiswa_2012))
print("Jenis Kelamin : ", jenis_kelamin_2012, "|" , "Tipe :", type(jenis_kelamin_2012))
print("Alamat Domisili :", alamat_2012,"|", "Tipe :", type(alamat_2012))
print("Umur :", umur_2012,"|", "Tipe :", type(umur_2012))
print("Skor Tes Awal :", skor_tes_awal_2012, "|", "Tipe :", type(skor_tes_awal_2012))
id_token_sinyal_2012 =100+3j
print("ID Token Sinyal :", id_token_sinyal_2012, "|" ,"Tipe :", type(id_token_sinyal_2012))
print( " " )
print("=== STATUS KELULUSAN PRATIKUM ===")
print("Batas Minimum Nilai :", batas_lulus_2012)
print("Dinyatakan Lulus?:", skor_tes_awal_2012 >= batas_lulus_2012, "|", "Tipe: ", type(skor_tes_awal_2012 >= batas_lulus_2012))