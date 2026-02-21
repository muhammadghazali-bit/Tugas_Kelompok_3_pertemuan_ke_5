# conditional statement
usia = 17
if usia >= 18:
    print("Status: Dewasa")
elif usia >= 13:
    print("Status: Remaja")
else:
    print("Status: Anak-anak")
    
password = "Jalangkote"
if password == "Jalangkote":
    print("Login berhasil")
    print("Selamat datang!")
print("Terima kasih telah menggunakan sistem")

pin = input("Masukkan PIN: ")
if pin == "Jalangkote":
    print("PIN benar")
else:
    print("PIN salah")

def cek_hari(angka):
    if angka == 1:
        print("Senin")
    elif angka == 2:
        print("Selasa")
    elif angka == 3:
        print("Rabu")
    elif angka == 4:
        print("Kamis")
    elif angka == 5:
        print("Jumat")
    elif angka == 6:
        print("Sabtu")
    elif angka == 7:
        print("Ahad")
    else:
        print("Hari tidak valid")

cek_hari(1)
cek_hari(2)
cek_hari(3)
cek_hari(4)
cek_hari(5)
cek_hari(6)
cek_hari(7)

nilai = int(input("Masukkan nilai: "))
if nilai >= 80:
    print("Lulus")
elif nilai >= 55:
    print("Remedial")
else:
    print("Tidak Lulus")
    
umur = int(input("Masukkan umur: "))
if umur >= 17:
    print("Boleh membuat SIM")
    if umur >= 21:
        print("Boleh membuat semua jenis SIM")
    else:
        print("Hanya boleh membuat SIM tertentu")
else:
    print("Belum cukup umur untuk membuat SIM")
    
umur = int(input("Masukkan umur: "))
pelajar = input("Apakah Anda pelajar? (ya/tidak): ")
if umur >= 17 and pelajar == "ya":
    print("Anda berhak mendapatkan diskon pelajar")
elif umur >= 17 and pelajar == "tidak":
    print("Anda tidak mendapatkan diskon pelajar")
else:
    print("Anda belum cukup umur")
    
umur = int(input("Masukkan umur: "))
kategori = "Dewasa" if umur >= 18 else "Belum Dewasa"
print(f"Anda termasuk {kategori}")

#Boolean (bool)
lampu_on = False
if lampu_on:
    print("Lampu mati")
    
#Angka (int, float)
umur = 20
if umur >= 18:
    print("Dewasa")
elif umur < 18:
    print("Belum dewasa")
    
#String (str)
Komentar = "Bagus!"
if Komentar:
    print("Komentar diterima")
    
#List, Tuple, Set, Dictionary
belanja = ["mie instan", "roti", "kopi"]
if belanja:
    print("Daftar belanja tersedia")
else:
    print("Daftar belanja kosong")
    
#NoneType (None)
pembayaran = None
if pembayaran is None:
    print("Pembayaran belum dilakukan")