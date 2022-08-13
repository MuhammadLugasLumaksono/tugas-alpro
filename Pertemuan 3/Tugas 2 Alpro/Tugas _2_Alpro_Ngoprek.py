# Tugas 2 Alpro
# Dik : dua buah algoritma menjelaskan sikap yang harus dilakukan jika menemukan lampu pengatur lalu lintas ( traffic lights ) di jalan raya : 
# 1.
#   if traffic lights menyala then
#	    if lampu merah then
#		    berhenti
#	    else
#		    jalan
# 2.      
#	if traffic lights menyala then
#	    if lampu merah then
#		    berhenti
#   else
#	    jalan


# Dit : 1. Pada keadaan apa kedua algoritma itu menggambarkan perilaku berbeda ? jelaskan !
#       2. Algoritma mana yang menurut Anda memuaskan ?
#       3. Silakan dicoba di VSCode menggunakan bahasa Python, kemudia screenshot hasilnya, lalu dilampirkan di file tugas !

#  Jwb :

# Cara 1
#merah = True

#if merah :
#    print (" berhenti ")
#else :
#    print (" jalan ")

# Cara 2
#merah = False

#if merah :
#    print (" berhenti ")
#else :
#    print (" jalan ")


# Cara 3
#traffic_lights = input("Input Warna Lampu ( merah, kuning, hijau ) = ")

#if traffic_lights == "merah":
#    print(" berhenti ")
#elif traffic_lights == "kuning":
#    print(" hati-hati ")
#elif traffic_lights == "hijau":
#    print(" jalan ")


# Cara 4
#traffic_lights = input(" Traffic Lights ( Mati / Menyala ) = ")
#lampu = input(" Lampu ( Merah / Kuning / Hijau ) = ")

#if traffic_lights == "Menyala":
#    print(" Traffic Lights Menyala ")
#if lampu == "Merah":
#        print(" Lampu Merah Menyala ( Berhenti ) ")
#else:
#		print(" Lampu Merah Mati ( Jalan ) ")

# Cara 5
traffic_lights_menyala = True
lampu_merah = True

if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
    else:
        print("Jalan")

traffic_lights_menyala = True
lampu_merah = True

if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
else:
    print("Jalan")

# Jwb :
# 1. Kedua algoritma itu menggambarkan perilaku berbeda pada keadaan membaca aksi ke-2 ( else ) :
#   1). Pada Algoritma pertama, posisi kondisi if, dan else dari variabel lampu_merah sudah sejajar, atau yang berarti sudah dapat menjalankan pemilihan dengan benar.
#       Jika variabel lampu_merah = True, maka kondisi ( if lampu_merah = True ) dibaca, kemudian aksi dari kondisi ( if lampu_merah = True ) diprint. Dan jika variabel lampu_merah = False, maka kondisi ( else lampu_merah = False ) dibaca, kemudian aksi dari kondisi ( else lampu_merah = False ) diprint.
#   2). Algoritma ke-dua, posisi kondisi if dan else dari variabel lampu_merah tidak sejajar, atau yang berarti tidak dapat menjalankan pemilihan dengan benar. 
#       Jika variabel lampu_merah = True, maka kondisi ( if lampu_merah = True) dibaca, kemudian aksi dari kondisi ( if lampu_merah = True) diprint. Dan jika variabel lampu_merah = False, maka kondisi ( else lampu_merah = False ) tidak dibaca, kemudian aksi dari kondisi ( else lampu_merah = False ) tidak diprint.
# 2. Algoritma yang menurut saya memuaskan adalah algoritma yang pertama, karena susunan kondisi dan aksi pada algoritma yang pertama sudah rapih. yaitu kondisi if dari variabel traffic_lights berada pada kolom terpisah dengan kondisi if dan else dari variabel lampu_merah yang berada pada kolom yang sejajar. Cara Kerja dari Algoritma tersebut adalah membaca variabel traffic_lights_menyala, kemudian membaca kondisi if traffic_lights_menyala, kemudian membaca kondisi if dan aksi if lampu_merah = True jika variabel lampu_merah = True, kemudian membaca kondisi else dan aksi else lampu_merah = False jika variabel lampu_merah = False.













