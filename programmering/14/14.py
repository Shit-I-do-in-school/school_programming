while 1:
    try:
        x, y, z = int(input("Mata in start! ")), int(input("Mata in stop! ")), int(input("Mata in steg! "))
    except:
        print("Error!!! SKRIV EN SIFRA ANARS FUNKAR JAG INTE MUAHAHAHA")
    else:
        for i in range(x, y+z, z):
            print(i)
        break