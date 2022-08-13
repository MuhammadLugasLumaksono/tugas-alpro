'''
Tugasnya adalah membuat database data nama orang
Nama_orang = [] 
1. show_data (kalau kosong tampilkan tulisan “Data Kosong”)
2. Insert_data
3. Delete_data
4. Edit_data
5. Exit
Pilih Menu : 1 (if dan else)
Apakah anda ingin memilih menu lagi (Y/N) : N (while)
'''
# Variabel Global
print("Variabel Global")
var ='Hello world'
def my_function():
  print(var)
my_function()

print("==============")

# Variabel Lokal
print("Variabel Lokal")
def my_function():
    var='Hello world'
    print(var)
my_function()

print("==============")

print("Lingkup Variabel Lokal dan Global / Variabel Lokal diprioritaskan")
var='global scope'
def my_function():
    var='local scope'
    print(var)
my_function()
print(var)

print("==============")

print("Mengubah Variabel Global di dalam fungsi")
var='global scope'
def my_function():
    global var
    print(var)
    var='local scope'
my_function()
print(var)

print("==============")

print("Fungsi Tanpa Parameter")
def salam(): # salam = nama fungsi 
    print("Hello, Selamat Pagi") # body fungsi
    # perbedaan letak kolom = indentansi ( contohnya adalah def dengan print atau print dengan salam )
salam()

print("==============")

print("Fungsi Dengan Parameter")
def salam(ucapan):
    print(ucapan)
salam("Selamat siang")

# Membuat fungsi dengan parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("Luas segitiga: %f" % luas)
# Pemanggilan fungsi
luas_segitiga(4, 6)

print("==============")

print("Fungsi Mengembalikan Nilai / return")
def luas_persegi(sisi): # sisi = parameter / input
    luas = sisi * sisi
    return luas # hasil pemrosesan
# pemanggilan fungsi
print ("Luas persegi: %d" % luas_persegi(6))

# Contoh Mencari Perbedaan di kedua program

# rumus: sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi

