list_nama = []
choice = ''
x = ''
y = ''
while choice != 'N' and choice != 'n':
    choice = input("input menu ( show data, insert data, remove data, edit data ) = ")
    if choice == 'show data':
        if len(list_nama) == 0:
            print("show data : data kosong")
        else:
            print("show data : ", list_nama)
    elif choice == 'insert data':
        x = str(input("input data yang ingin ditambah = "))
        list_nama.append(x)
        print("insert data : ", list_nama)
    elif choice == 'remove data':
        x = str(input("input data yang ingin diremove = "))
        list_nama.remove(x)
        print("remove data : ", list_nama)
    elif choice == 'edit data':
        y = int(input("input data ke-berapa yang ingin diedit = "))
        x = str(input("input data yang ingin ditambah ke list = "))
        list_nama[y] = (x)
        print("edit data : ", list_nama)
    else:
        print("menu yang anda pilih tidak tersedia")
print("pemilihan selesai, terima kasih sudah memberikan respon")

