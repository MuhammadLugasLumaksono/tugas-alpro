# 1
a = int(input("Input Panjang a = "))
b = int(input("Input Panjang b = "))
c = int(input("Input Panjang c = "))

if a == b == c:
    print("Segitiga Sama Sisi ( Equilateral Triangle )")
elif a == c:
    print("Segitiga Sama Kaki ( Isosceles Triangle) ")
elif a < b > c or a > b < c or a < b < c or a > b > c: 
    print("Segitiga Sembarang ( Scalene Triangle )")

# 2
Tahun = int(input("Input Tahun = "))
Jenis_Tahun = str()

if Tahun % 400 == 0:
    Jenis_Tahun = "termasuk tahun kabisat"
elif Tahun % 400 != 0 and Tahun % 100 == 0:
    Jenis_Tahun = "tidak termasuk tahun kabisat"
elif Tahun % 400 != 0 and Tahun % 100 != 0 and Tahun % 4 == 0:
    Jenis_Tahun = "termasuk tahun kabisat"
elif Tahun % 400 != 0 and Tahun % 100 != 0 and Tahun % 4 != 0:
    Jenis_Tahun = "tidak termasuk tahun kabisat"
print(f"{Tahun} {Jenis_Tahun}")

# 3
Tanggal = int(input("Input Tanggal = "))
Bulan = input("Input Bulan = ")
Tahun = int(input("Input Tahun = "))
Zodiak_Saya = str()
if Tanggal < 22 and Bulan == 'Desember' or Tanggal > 22 and Bulan == 'November':
    Zodiak_Saya = 'Sagitarius' 
elif Tanggal < 20 and Bulan == 'Januari' or Tanggal > 21 and Bulan == 'Desember':
    Zodiak_Saya = 'Kaprikornus'  
elif Tanggal < 19 and Bulan == 'Februari' or Tanggal > 19 and Bulan == 'Januari': 
    Zodiak_Saya = 'Akuarius'
elif Tanggal < 21 and Bulan == 'Maret' or Tanggal > 18 and Bulan == 'Februari':  
    Zodiak_Saya = 'Pises'  
elif Tanggal < 20 and Bulan == 'April' or Tanggal > 20 and Bulan == 'Maret':
    Zodiak_Saya = 'Aries'  
elif Tanggal < 21 and Bulan == 'Mei' or Tanggal > 19 and Bulan == 'April': 
    Zodiak_Saya = 'Taurus'
elif Tanggal < 21 and Bulan == 'Juni' or Tanggal > 20 and Bulan == 'Mei':  
    Zodiak_Saya = 'Gemini'  
elif Tanggal < 23 and Bulan == 'Juli' or Tanggal > 20 and Bulan == 'Juni':
    Zodiak_Saya = 'Cancer'
elif Tanggal < 23 and Bulan == 'Agustus' or Tanggal > 22 and Bulan == 'Juli': 
    Zodiak_Saya = 'Leo'
elif Tanggal < 23 and Bulan == 'September' or Tanggal > 22 and Bulan == 'Agustus':
    Zodiak_Saya = 'Virgo'
elif Tanggal < 23 and Bulan == 'Oktober' or Tanggal > 22 and Bulan == 'September':
    Zodiak_Saya = 'Libra'  
elif Tanggal < 23 and Bulan == 'November' or Tanggal > 22 and Bulan == 'Oktober':
    Zodiak_Saya = 'Scorpio'
print(f"Saya lahir pada {Tanggal} {Bulan} {Tahun}, dan zodiak saya adalah {Zodiak_Saya}")