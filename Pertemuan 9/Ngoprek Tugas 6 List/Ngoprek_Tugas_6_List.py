#Ngoprek

# 1  
# Membuat list jenis hobi sebanyak 10 
# > Tampilkan isi list indeks no. 3-5 
# > Tampilkan semua hobi dengan perulangan 
# > Tampilkan panjang list
jenis_hobi = ["Membaca","Menulis","Olahraga","Memasak","Menyanyi","Bermain","Mendaki","Berkebun","Beternak","Memancing"]
print("jenis hobi antara data ke-3 sampai ke-5 :", jenis_hobi[3:5] )
input_list_jenis_hobi = str(input("apakah ingin melihat list jenis hobi ?"))
if input_list_jenis_hobi == "iya" or input_list_jenis_hobi == "Iya" or input_list_jenis_hobi == "IYA":
    print("list jenis hobi :",jenis_hobi)
print("banyak data dalam list = ",len(jenis_hobi))

# 2
# Membuat program input hobi dengan pengulangan sampai input selesai
# Tampilkan hasil inputan 
'''list_hobi = []
input_hobi = ''
pilihan = ''
while pilihan != "T" and pilihan != "t":
    pilihan = input("Apakah akan menginput hobi ? = ")
    if pilihan == "Y" or pilihan == "y":
        input_hobi = input("Input hobi = ")
        list_hobi.append(input_hobi)
    elif pilihan == "Y" or pilihan == "y":
        input_hobi = input("Input hobi = ")
        list_hobi.append(input_hobi)
    elif pilihan == "Y" or pilihan == "y":
        input_hobi = input("Input hobi = ")
        list_hobi.append(input_hobi)
    elif pilihan == "Y" or pilihan == "y":
        input_hobi = input("Input hobi = ")
        list_hobi.append(input_hobi)
    else:
        print("=================")
        print(list_hobi)
        print("Anda memiliki 4 hobi : ")
        print("-",list_hobi[0])
        print("-",list_hobi[1])
        print("-",list_hobi[2])
        print("-",list_hobi[3])'''

list_hobi = []
input_hobi = ''
pilihan = ''
while pilihan != "T" and pilihan != "t":
    pilihan = input("Apakah akan menginput hobi ? = ")
    if pilihan == "Y" or pilihan == "y":
        input_hobi = input("Input hobi = ")
        list_hobi.append(input_hobi)
    else:
        print("=================")
        print(list_hobi)
        print("Anda memiliki 4 hobi : ")
        print("-",list_hobi[0])
        print("-",list_hobi[1])
        print("-",list_hobi[2])
        print("-",list_hobi[3])


# 3
# Menghapus string kosong dari list string berikut : 
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
del list1[1]
del list1[3]
print("list string setelah string kosong dihapus =",list1)

# 4 
# Menambah item 7000 setelah 6000
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# menjadi list1 = [10, 20, [300, 400, [5000, 6000,7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print("list ke-2 dan ke-3 =",list1[2])
print("list ke-3 =",list1[2][2])
list1[2][2].append(7000)
print("list setelah penambahan item 7000 =",list1)

# 5
# Mencari item 20 dari list
# Jika ada, gantilah item 20 dengan 200
# Kemudian, hanya kejadian pertama dari suatu nilai yang akan diupdate
# list1 = [5, 10, 15, 20, 25, 50, 20]
list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1)
index = list1.index(int(input("masukkan nilai = ")))
print("Indeks dari nilai = ", index)
list1[index] = 200
print(list1)
