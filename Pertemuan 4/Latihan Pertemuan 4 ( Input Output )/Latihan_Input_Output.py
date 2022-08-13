# Latihan Pertemuan 4 ( Input Output )



#Ngoprek 1

while True:
    Nama = input("Input Nama = ")
    Prodi = input("Input Prodi = ")
    NIM = int(input("Input NIM = "))
    Input_Nilai_Mata_Kuliah_Alpro = int(input("Input Nilai Mata Kuliah Alpro = "))
    Hasil_Nilai_Mata_Kuliah_Alpro = str()

    if Input_Nilai_Mata_Kuliah_Alpro > 80:
        Hasil_Nilai_Mata_Kuliah_Alpro = "A"
    elif Input_Nilai_Mata_Kuliah_Alpro > 70 and Input_Nilai_Mata_Kuliah_Alpro <= 80:
        Hasil_Nilai_Mata_Kuliah_Alpro = "AB"
    elif Input_Nilai_Mata_Kuliah_Alpro > 65 and Input_Nilai_Mata_Kuliah_Alpro >= 70:
        Hasil_Nilai_Mata_Kuliah_Alpro = "B"
    elif Input_Nilai_Mata_Kuliah_Alpro > 60 and Input_Nilai_Mata_Kuliah_Alpro >= 65:
        Hasil_Nilai_Mata_Kuliah_Alpro = "BC"
    elif Input_Nilai_Mata_Kuliah_Alpro > 55 and Input_Nilai_Mata_Kuliah_Alpro >= 60:
        Hasil_Nilai_Mata_Kuliah_Alpro = "C"
    elif Input_Nilai_Mata_Kuliah_Alpro > 40 and Input_Nilai_Mata_Kuliah_Alpro >= 55:
        Hasil_Nilai_Mata_Kuliah_Alpro = "D"
    elif Input_Nilai_Mata_Kuliah_Alpro >= 40:
        Hasil_Nilai_Mata_Kuliah_Alpro = "E"
    else:
        Hasil_Nilai_Mata_Kuliah_Alpro = "tidak memenuhi kriteria, maka saya tidak lulus mata kuliah Alpro"
    
    print(f"Nama saya {Nama}\nSaya dari Prodi {Prodi}\nNIM saya {NIM}\nNilai Mata Kuliah Alpro saya {Hasil_Nilai_Mata_Kuliah_Alpro}")

    pengulangan = input("Apakah ingin melakukan pengulangan? = ")
    if pengulangan == "Iya" or pengulangan == "iya":
        continue
    elif pengulangan != "Iya":
        print("Terima kasih sudah bersedia memberikan data")
        break




"""
# Ngoprek 2 ( Belum Paten ) 

Banyak_Data = int(input("Banyak data yang akan diinput = "))

Nama = []
Program_Studi = []
NIM = []
Input_Nilai_Mata_Kuliah_Alpro = []
Hasil_Nilai_Mata_Kuliah_Alpro = []

for x in range ( 0, Banyak_Data ):
    print(f"Data ke-{x}")
    Input_Nama = input("Nama = ")
    Input_Program_Studi = input("Program Studi = ")
    Input_NIM = int(input("NIM = "))
    Input_Nilai_Mata_Kuliah_Alpro = int(input("Nilai Matkul Alpro = ")) 
       
if Input_Nilai_Mata_Kuliah_Alpro > 80:
    Hasil_Nilai_Mata_Kuliah_Alpro = "A"
elif Input_Nilai_Mata_Kuliah_Alpro > 70 and Input_Nilai_Mata_Kuliah_Alpro <= 80:
    Hasil_Nilai_Mata_Kuliah_Alpro = "AB"
elif Input_Nilai_Mata_Kuliah_Alpro > 65 and Input_Nilai_Mata_Kuliah_Alpro >= 70:
    Hasil_Nilai_Mata_Kuliah_Alpro = "B"
elif Input_Nilai_Mata_Kuliah_Alpro > 60 and Input_Nilai_Mata_Kuliah_Alpro >= 65:
    Hasil_Nilai_Mata_Kuliah_Alpro = "BC"
elif Input_Nilai_Mata_Kuliah_Alpro > 55 and Input_Nilai_Mata_Kuliah_Alpro >= 60:
    Hasil_Nilai_Mata_Kuliah_Alpro = "C"
elif Input_Nilai_Mata_Kuliah_Alpro > 40 and Input_Nilai_Mata_Kuliah_Alpro >= 55:
    Hasil_Nilai_Mata_Kuliah_Alpro = "D"
elif Input_Nilai_Mata_Kuliah_Alpro >= 40:
    Hasil_Nilai_Mata_Kuliah_Alpro = "E"
else:
    Hasil_Nilai_Mata_Kuliah_Alpro = "Tidak Lulus Mata Kuliah Alpro"

    Nama.append(Input_Nama)
    Program_Studi.append(Input_Program_Studi)
    NIM.append(Input_NIM)
    Hasil_Nilai_Mata_Kuliah_Alpro.append(Input_Nilai_Mata_Kuliah_Alpro)

for x in range(0, len(Nama)):
    Data_Nama = Nama[x]
    Data_Program_Studi = Program_Studi[x]
    Data_NIM = NIM[x]
    Data_Hasil_Nilai_Mata_Kuliah_Alpro = Hasil_Nilai_Mata_Kuliah_Alpro[x]
    print(f"Hasil Data :\n Nama saya {Data_Nama} \nSaya dari Prodi {Data_Program_Studi} \nNIM saya {Data_NIM} \nNilai Mata Kuliah Alpro saya {Data_Hasil_Nilai_Mata_Kuliah_Alpro}")
"""





