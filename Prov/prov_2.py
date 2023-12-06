
#gör en funktion som sparar summa till text filen
def spara(nummer):
    nummer = str(nummer)
    with open("savedNr.txt", "w") as f:
        f.write(nummer)
        
#få in det senaste tallet från txt filen så vi kan skriva ut den i print("Tidigare summa = ", tidigare())      
def tidigare():
    with open("savedNr.txt", "r") as f:
        z = int(f.read())
    return z     


while 1:
    #printar ut summan som finns i txt filen
    print("Tidigare summa = ", tidigare())
    #tar in siffra eller bokstaven A så att vi kan kolla om vi ska addera siffrorna eller stänga av pogramet.
    i = input("Lägg till ett nytt tal till en summa (eller avsluta med a)\nSkriv talet (eller A): ")
    #kollar så att bokstaven A är en stor bokstav. 
    if i.lower() != "a":
        #tästar om vi kan addera siffrorna annars går den till execpt: print("Det är ingen tal")
        try:
            y = int(i)
            z = tidigare() + y 
            spara(z)
        # printar att det inte är en siffra om du skrev in ett tal
        except: print("Det är ingen tal")
        #om vi får in ett A från inputen så kör vi koden under denna kommentar
    else:
       print("Nu avslutar programmet!")
       break