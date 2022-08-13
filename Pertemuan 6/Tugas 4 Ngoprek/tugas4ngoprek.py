'''
Buatlah program menggunakan pengkondisian (While Loop, For Loop, Nested Loop) dengan skenario sebagai berikut :
Program 1, memfilter bilangan genap dan ganjil dari suatu list kemudian menjumlahkan berapa jumlah bilangan genap & ganjil nya
Program 2, menampilkan nilai perkalian dari masukkan nilai, seperti pada gambar
Program 3, perkalian nilai 1-100
'''

# 1
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
a = 6
for i in range(0, a):
    for j in range(0, a - 1):
        print('* ' , end='')
    a -= 1
    print('')
print("\n")
'''
string = ""

bar = int(input("Masukkan angka :"))
no = bar
# Looping Baris
while bar >= 0:
	# Looping Kolom
	kol = bar
	while kol > 0:
		string = string + " " + str(no) + " "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar - 1
	no = no - 1
print (string)
'''

# 5 
print("Nomor 5")
a = 4
for i in range(0, a):
    for j in range(0, 1 + i):
        print('* ' , end='')
    print('')

'''
string = ""
bar = 1

x = int(input("Masukkan angka :"))
no = 1
# Looping Baris
while bar <= x:
	kol = bar
	# Looping Kolom
	while kol > 0:
		string = string + " " + str(no) + " "
		kol = kol - 1

	string = string + "\n"
	bar = bar + 1
	no = no+1
print (string)
'''
