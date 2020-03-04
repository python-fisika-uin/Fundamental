# Sintaks Sekuensial
print('Hello World!')
nama = 'Eko S.W'
usia = 40
Usia = 50 #ini berbeda dengan usia (huruf kecil)
print(nama, 'Usia=', usia)

# Sintaks bercabang
if usia <= 40:
  print('Masih muda')
  print('Usia belajar')
  print('Usia mencari jatidiri')
else:
  print('Tak muda lagi')
  print('Banyakin tobat')
  print('Pikir anak cucu')

#sintaksis perulangan
jumlah_anak = 2
for iterasi in range(1, jumlah_anak+1):
  print('Halo anak ke', iterasi)

# contoh lain: menghitung 1+2+3+4+5 = 15
jumlah_bilangan = 5
total_penjumlahan = 0
for bilangan in range(1, jumlah_bilangan+3):
  total_penjumlahan = total_penjumlahan + bilangan
print('Hasil penjumlahan', total_penjumlahan)

# cara membaca baris ke 27
"""
1. total_penjumlahan = 0 + 1 = 1
2. total_penjumlahan = 1 + 2 = 3
3. total_penjumlahan = 3 + 3 = 6
4. total_penjumlahan = 6 + 4 = 10
5. total_penjumlahan = 10 + 5 = 15
6. total_penjumlahan = 15 + 6 = 21
7. total_penjumlahan = 21 + 7 = 28

"""  
#tipe data array
uang_untuk_anak = [] #tipe data array
uang_untuk_anak.append(10000)
uang_untuk_anak.append(5000)
uang_untuk_anak.append(50000)

# berapa rata2 uang untuk tiap anak?
jumlah_total_uang = 0
for uang in uang_untuk_anak:
  jumlah_total_uang = jumlah_total_uang + uang
  
print('Jumlah total uang', jumlah_total_uang)
rata_rata_uang = jumlah_total_uang / 3
print('Rata-rata uang', rata_rata_uang)
