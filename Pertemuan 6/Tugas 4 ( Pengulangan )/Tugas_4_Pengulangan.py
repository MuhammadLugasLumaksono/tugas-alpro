'''
Buatlah program menggunakan pengkondisian (While Loop, For Loop, Nested Loop) dengan skenario sebagai berikut :
Program 1, memfilter bilangan genap dan ganjil dari suatu list kemudian menjumlahkan berapa jumlah bilangan genap & ganjil nya
Program 2, menampilkan nilai perkalian dari masukkan nilai, seperti pada gambar
Program 3, perkalian nilai 1-100
'''

# 1 ( memfilter bilangan genap dan ganjil dari suatu list kemudian menjumlahkan berapa jumlah bilangan genap & ganjil nya )
print("Nomor 1")            
nilai = int(input("Masukkan angka = "))
input_angka = []
bilangan_genap = []
bilangan_ganjil = []
for x in range(1, nilai):
    if x:
        input_angka.append(x)
    if x % 2 == 0:
        bilangan_genap.append(x)
    if x % 2 == 1:
        bilangan_ganjil.append(x)
print('List angka = ', input_angka)
print("Bilangan genap = ", bilangan_genap)
print("Banyak bilangan genap = ", len(bilangan_genap))
print("Bilangan ganjil = ", bilangan_ganjil)
print("Banyak bilangan ganjil = ", len(bilangan_ganjil))
print("\n")

# 2 ( menampilkan nilai perkalian dari masukkan nilai, seperti pada gambar ) 
print("Nomor 2")
bilangan = int(input("Input angka = "))
for i in range(1,11):
    hasil = bilangan * i
    print(bilangan, "x", i, "=", hasil)
print("\n")

# 3 ( perkalian nilai 1-100 )
print("Nomor 3")
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()
print("\n")

# 4 
print("Nomor 4")
x = int(input("Masukkan angka = "))
for i in range ( 1, x + 1):
    for j in range ( 1, x + 1):
        print ( j, end=' ')
    print()
    x-=1
print("\n")

# 5 
print("Nomor 5")
x = int(input("Masukkan angka = "))
y = 1
z = 1
while ( z < 5 ):
    a = 1
    while ( a <= z ):
        print(str(y) + ' ', end=' ')
        y+=1
        a+=1
    print(' ')
    z+=1