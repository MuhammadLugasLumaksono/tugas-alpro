# Tugas 2 Alpro

# Algoritma 1
traffic_lights_menyala = True
lampu_merah = True
if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
    else:
        print("Jalan")

traffic_lights_menyala = True
lampu_merah = False

if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
    else:
        print("Jalan")        

# Algoritma 2
traffic_lights_menyala = True
lampu_merah = True

if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
else:
    print("Jalan")

traffic_lights_menyala = True
lampu_merah = False

if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
else:
    print("Jalan")    

# Algoritma 1 ( Input )
"""
traffic_lights = input(" Traffic Lights ( Mati / Menyala ) = " )
lampu_merah = input( " Lampu Merah ( Mati / Menyala ) = " )

if traffic_lights == "Menyala":
    if lampu_merah == "Menyala":
        print("Berhenti")
    else:
        print("Jalan")        
"""

# Algoritma 2 ( Input )
"""
traffic_lights = input(" Traffic Lights ( Mati / Menyala ) = " )
lampu_merah = input( " Lampu Merah ( Mati / Menyala ) = " )

if traffic_lights == "Menyala":
    if lampu_merah == "Menyala":
        print("Berhenti")
else:
    print("Jalan")
"""

# Algoritma 1 ( Boolean 3 Lampu )
"""
traffic_lights_menyala = True 
lampu_merah = True
lampu_kuning = True
lampu_hijau = True
if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
    elif lampu_kuning:
        print("Bersiap-siap")
    else:
        print("Jalan")    

traffic_lights_menyala = True 
lampu_merah = True
lampu_kuning = True
lampu_hijau = True
if traffic_lights_menyala:
    if lampu_merah == False: # Contoh Input boolean di kondisi
        print("Berhenti")
    elif lampu_kuning == True:
        print("Bersiap-siap")
    else:
        print("Jalan")    
"""

# Algoritma 2 ( Boolean 3 Lampu )
"""
traffic_lights_menyala = True 
lampu_merah = True
lampu_kuning = True
lampu_hijau = True

if traffic_lights_menyala:
    if lampu_merah:
        print("Berhenti")
    elif lampu_kuning:
        print("Bersiap-siap")
else:
    print("Jalan")
"""

# Algoritma 1 ( Input 3 Lampu )
"""
traffic_lights = input(" Traffic Lights ( Mati / Menyala ) = ")
lampu = input(" Lampu ( Merah / Kuning / Hijau ) = ")
if traffic_lights == "Menyala":
    if lampu == "Merah":
        print("Berhenti")
    elif lampu == "Kuning":
        print("Bersiap-siap")      
    else:
        print("Jalan")
"""

# Algoritma 2 ( Input 3 Lampu )
"""
traffic_lights = input(" Traffic Lights ( Mati / Menyala ) = ")
lampu = input(" Lampu ( Merah / Kuning / Hijau ) = ")

if traffic_lights == "Menyala":
    if lampu == "Merah":
        print("Berhenti")
    elif lampu == "Kuning":
        print("Bersiap-siap")      
else:
    print("Jalan")
"""





