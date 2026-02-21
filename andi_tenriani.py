#transfer statement 
def hitung_rata(nilai_rapor, nilai_sikap, nilai_ujian):
    return (nilai_rapor + nilai_sikap + nilai_ujian) / 3
#Input nilai
nilai_rapor = int(input("Masukkan Nilai Rapor: "))
nilai_sikap = int(input("Masukkan Nilai Sikap: "))
nilai_ujian = int(input("Masukkan Nilai Ujian: "))

# Panggil fungsi
rata = hitung_rata(nilai_rapor, nilai_sikap, nilai_ujian)
print("Rata-rata Nilai:", rata)

# Pass
if rata >= 75:
    print("Status: Lulus")
elif rata >= 60:
    pass   
else:
    print("Status: Mengulang")