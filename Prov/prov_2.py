import os

#gör en funktion som skapar filen savedNr.txt
def skapafil():
    
    #försöker skapa filen
    try: open("savedNr.txt", "x")
    
    #ger error om filen finns
    except FileExistsError: print("Filen finns redan")
    
    except Exception as e: print("Error: ", e)
    #om inga error händer skapas filen och det printar ut att den är skapad
    else: print("Filen skapats")


def readfile():
    #här öppnar vi filen och läser inehållet
    f = open("savedNr.txt", "r")
    #här printar vi ut texten som är i filen
    print("Tidigare summa", f.read())
    
    f = open("savedNr.txt", "w")
    
    f.write("0")
    
    f.close()

def writefile():
    f = open("savedNr.txt", "w")
    f.write()

skapafil()
readfile()

while 1:
    i = input("Lägg till ett nytt tal till en summa (eller avsluta med a)\nSkriv talet (eller A): ")
    if i == "a" or "A":
        quit()
#    elif input == 
 #      writefile()