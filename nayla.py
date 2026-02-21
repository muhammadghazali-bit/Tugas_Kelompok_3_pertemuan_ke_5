# iterative statement

#perbedaan for dan while
#kasus for (jumlah sudah pasti)
for i in range(8):
    print("(for)perulangan ke-", i)

# Kasus while
i = 0
while i < 10:
    print("(while) perulangan ke-", i)
    i += 1

# Break
for i in range(40):
    if i == 20:
        break
    print("Break:", i)

# Continue
for i in range(18):
    if i == 9:
        continue
    print("continue:", i )

# Else di loop
for angka in range(12):
    print(angka)
else:
    print("Loop selesai, tidak ada break")

# Nested di loop
for baris in range(6):
    for kolom in range(4):
        print(baris, kolom)

# Membuat pola bintang
for baris in range(8):
    for kolom in range(baris + 1):
        print("*", end="")
    print()

# menghitung jumlah total
data = [15, 25, 35, 45]
jumlah = 0

for nilai_data in data:
    jumlah += nilai_data

print("Total:", jumlah)

n = 5
faktorial = 1

for i in range(1, n+1):
    faktorial *= i

print("Faktorial:", faktorial)

#Validasi Input dengan while
angka = -2

while angka < 0:
    angka = int(input("Masukkan bilangan positif: "))

print("Data sudah diterima")


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