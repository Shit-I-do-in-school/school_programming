while 1:
    try: x,y,z = int(input("Mata in start: ")), int(input("Mata in stop: ")), int(input("Mata in steg: "))
    except: print("Inamatad fel dada typ (inte siffra)")
    else:
        for i in range(x,y+z,z):
            print(i)
        break