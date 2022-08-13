# 1
hobi = ["Membaca","Menulis","Olahraga","Memasak","Menyanyi","Bermain","Mendaki","Berkebun","Beternak","Memancing"]
print("data ke-3 sampai ke-5 dari list hobi :", hobi[3:5] )
input_data_list_hobi = str(input("apakah ingin melihat list hobi ? = "))
if input_data_list_hobi == "iya" or input_data_list_hobi == "Iya" or input_data_list_hobi == "IYA":
    print("list hobi :",hobi)
print("banyak data dalam list hobi = ",len(hobi))

# 2
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
        print("Anda memiliki 4 hobi : ")
        print("-",list_hobi[0])
        print("-",list_hobi[1])
        print("-",list_hobi[2])
        print("-",list_hobi[3])

# 3
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list1)
del list1[1]
del list1[3]
print("list string setelah string kosong dihapus =",list1)

# 4 
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print("list1 = ",list1)
print("list ke-2 dan ke-3 =",list1[2])
print("list ke-3 =",list1[2][2])
list1[2][2].append(7000)
print("list setelah penambahan item 7000 =",list1)

# 5
list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1)
index = list1.index(int(input("input nilai = ")))
print("indeks dari nilai inputan = ", index)
list1[index] = 200
print("list setelah nilai 20 dipastikan ada, dan diganti dengan nilai 200 = ",list1)