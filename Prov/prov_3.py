#spara det vi har skrivit till en fil så vi kan börja där när vi startar om pogrammet
#använde https://pynative.com/python-write-list-to-file/ för att hitta hur jag skulle spara en lista till text fil
def s(i):
    with open("SavedTxt.txt", "w") as fp:
        for items in i:
            fp.write(items + " ")

#vi öppnar text filen för att skriva ut i vår lista så vi kan fortsätta där vi slutade
#insperation från https://pythonhow.com/how/read-a-file-line-by-line-into-a-list/
def l():
    fileobj=open("SavedTxt.txt")
    #skapar en temporar lista
    line = []
    
    for lines in fileobj:
        for w in lines.split():
            line.append(w)
    return line

#gör så att list blir den gamla listan från senaste körning
list = l()
#printa ut gamla listan från text filen
print(list)
#en loop som inte slutar köras. Om du inte skriver in bokstaven (A) 
while 1:
    #ta input 
    i = input("Lägg till ett nytt ord eller index för ordet (eller avsuta med A) \n Skriv ordet (Eller A): ")
    #Om vi får i (A) så öppnar vi text filen och skriver in vår lista där
    try:
        index = int(i)
        print(list[index])
    #om du skriver ett nummer som är sturre eller - så kommer den säga att det inte existerar en sådan positon
    except IndexError:
        print("fel positon (den positionen existerar inte)")    
    except ValueError:
        #Om vi skriver (A) eller (a) så stänger den av pogrammet och printar ut listan som vi har
        if i.lower() != "a":
            list.append(i)
            print(list)
        else:
            #printa listan
            print(list)
            #sparar till listan så vi kan printa ut det igen
            s(list)
            break