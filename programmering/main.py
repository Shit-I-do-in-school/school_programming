# Spara senaste talen till filen
def save(nr):
    nr = str(nr)
    with open("savedNR.txt", "w") as f:
        f.write(nr)

def tidigareSum():# Lada in senaste talen och returna den
    with open("savedNR.txt", "r") as f:
        z = int(f.read())
    return z


while 1:
    print("Tidigare summa = ", tidigareSum())
    x = input("Lägg till ett nytt tal till en summa (eller avsluta med A) ")# ta input
    if x.lower() != "a":# kolla om den är a (A)
        try:# prova att omvandla den till siffra
            y = int(x)
            z = tidigareSum() + y# summera tal
            save(z)# spara till filen
        except: print("Det är ingen tal")# om det gick inte då är det ingen siffra
    else:
        print("Avslutat")
        print("Summan: ", tidigareSum())
        break# avsluta koden eftersom A skrevs in