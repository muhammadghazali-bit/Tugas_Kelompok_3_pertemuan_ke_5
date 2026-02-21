# import requests

# response = requests.get("https://gologin.com/managed-web-access/?utm_term=web%20data%20api&utm_campaign=gologin_" \
# "search_managed_web_access_ww&utm_source=google&utm_medium=cpc&utm_content=797037105322&gad_source=1&gad_campaignid=" \
# "23553879245&gbraid=0AAAAACMrawiFL29KabFK5z7wLoBb7M_bk&gclid=Cj0KCQiAqeDMBhDcARIsAJEbU9TwmtAqjDOwi7KTiTRm8YgaJyq3pPwXE" \
# "aRPTEzJm1nA3p83uqh2x0AaApC7EALw_wcB")

# print(response.status_code)
# print(response.text)


# import random

# angka = random.randint(1, 15)
# print("Angka acak:", angka)

##===========================================================

##conditional statement

# usia = 17
# if usia >= 18:
#     print("Status: Dewasa")
# elif usia >= 13:
#     print("Status: Remaja")
# else:
#     print("Status: Anak-anak")
    
# password = "Jalangkote"
# if password == "Jalangkote":
#     print("Login berhasil")
#     print("Selamat datang!")
# print("Terima kasih telah menggunakan sistem")

# pin = input("Masukkan PIN: ")
# if pin == "Jalangkote":
#     print("PIN benar")
# else:
#     print("PIN salah")

# def cek_hari(angka):
#     if angka == 1:
#         print("Senin")
#     elif angka == 2:
#         print("Selasa")
#     elif angka == 3:
#         print("Rabu")
#     elif angka == 4:
#         print("Kamis")
#     elif angka == 5:
#         print("Jumat")
#     elif angka == 6:
#         print("Sabtu")
#     elif angka == 7:
#         print("Ahad")
#     else:
#         print("Hari tidak valid")

# cek_hari(1)
# cek_hari(2)
# cek_hari(3)
# cek_hari(4)
# cek_hari(5)
# cek_hari(6)
# cek_hari(7)

# nilai = int(input("Masukkan nilai: "))
# if nilai >= 80:
#     print("Lulus")
# elif nilai >= 55:
#     print("Remedial")
# else:
#     print("Tidak Lulus")
    
# umur = int(input("Masukkan umur: "))
# if umur >= 17:
#     print("Boleh membuat SIM")
#     if umur >= 21:
#         print("Boleh membuat semua jenis SIM")
#     else:
#         print("Hanya boleh membuat SIM tertentu")
# else:
#     print("Belum cukup umur untuk membuat SIM")
    
# umur = int(input("Masukkan umur: "))
# pelajar = input("Apakah Anda pelajar? (ya/tidak): ")
# if umur >= 17 and pelajar == "ya":
#     print("Anda berhak mendapatkan diskon pelajar")
# elif umur >= 17 and pelajar == "tidak":
#     print("Anda tidak mendapatkan diskon pelajar")
# else:
#     print("Anda belum cukup umur")
    
# umur = int(input("Masukkan umur: "))
# kategori = "Dewasa" if umur >= 18 else "Belum Dewasa"
# print(f"Anda termasuk {kategori}")


#Boolean (bool)
# lampu_on = False
# if lampu_on:
#     print("Lampu mati")
    
#Angka (int, float)
# umur = 20
# if umur >= 18:
#     print("Dewasa")
# elif umur < 18:
#     print("Belum dewasa")
    
#String (str)
# Komentar = "Bagus!"
# if Komentar:
#     print("Komentar diterima")
    
#List, Tuple, Set, Dictionary
# belanja = ["mie instan", "roti", "kopi"]
# if belanja:
#     print("Daftar belanja tersedia")
# else:
#     print("Daftar belanja kosong")
    
#NoneType (None)
# pembayaran = None
# if pembayaran is None:
#     print("Pembayaran belum dilakukan")

##=================================================

## Interative statement

## Perulangan Menggunakan for loop
# for i in range(50):
#     print("Perulangan ke-", i)

## Pengulangan Menggunakan while loop
# i = 0
# while i < 5:
#     print("Perulangan ke-", i)
#     i += 1

## Break
# for perulangan in range(40):
#     if perulangan == 20:
#         break
#     print(perulangan)

## continue
# for perulangan in range(10):
#     if perulangan == 3:
#         continue
#     print(perulangan)

## Else di loop
# for angka in range(12):
#     print(angka)
# else:
#     print("Loop selesai, tidak ada break")

## Nested di loop
# for baris in range(6):
#     for kolom in range(4):
#         print(baris, kolom)

## Membuat pola bintang
# for baris in range(50):
#     for kolom in range(baris + 1):
#         print("-", end="")
#     print()

## menghitung jumlah total
# data = [15, 25, 35, 45]
# jumlah = 0

# for nilai_data in data:
#     jumlah += nilai_data

# print("Total:", jumlah)

# n = 5
# faktorial = 1

# for i in range(1, n+1):
#     faktorial *= i

# print("Faktorial:", faktorial)

##Validasi Input dengan while
# angka = -2

# while angka < 0:
#     angka = int(input("Masukkan bilangan positif: "))

# print("Data sudah diterima")

##========================================================

##transfer statement 

## Return statement
# def hitung_rata(nilai_rapor, nilai_sikap, nilai_ujian):
#     return (nilai_rapor + nilai_sikap + nilai_ujian) / 3
#Input nilai
# nilai_rapor = int(input("Masukkan Nilai Rapor: "))
# nilai_sikap = int(input("Masukkan Nilai Sikap: "))
# nilai_ujian = int(input("Masukkan Nilai Ujian: "))

# rata = hitung_rata(nilai_rapor, nilai_sikap, nilai_ujian)
# print("Rata-rata Nilai:", rata)

# ## Pass Statement
# if rata >= 75:
#     print("Status: Lulus")
# elif rata >= 60:
#     pass   
# else:
#     print("Status: Mengulang")



