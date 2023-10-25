import os

def Hola():
    print("öppna textfil: Skriv O ")
    print("Skapa textfil: Skriv C ")
    print("Avsluta pogram: Skriv A ")
    
    return input("Skriv vad du vill göra !?! ")

def MakeText():
    hola = input("Vad ska filen heta? ")
    try:
        hola = open( hola + ".txt", "x" )
    except FileExistsError: print("error filen finns redan.")
    else: print("Filen skapas :)")
    
def OpenFile():
    while 1:
        print("Vad vill du göra? ")
        print("Skapa rad I text fil: Skriv L ")
        print("skriva ut texten i filen: Skriv S ")
        print("radera filen: Skriv R ")
        print("Avsluta: Skriv A ")
        Val = input("Vad väljer du?! ")
        
        if Val == "r":  
            Epic = input("Klistra in fil namnet. ")
            f = open(Epic, "a")
            content = input("skriv vad du vill i filen! ")
            f.write(content)
            f.close()
        elif Val == "s":
            ad = input("Vad heter filen? ")
            f = open(ad, "r")
            print("Det står", f.read(), "I text filen")
            f.close()
        elif Val == "L":
            what = input("Klistra in fil namnet. ")
            f = open(what, "r")
            f.write("\n")
        elif Val == "R":
            asg = input("Klistra in fil namnet. ")
            os.remove(asg)
        elif Val == "A":
            quit()
    
while 1:
    cmd = Hola()
    if cmd == "C":
        MakeText()
    elif cmd == "O":
        OpenFile()
    elif cmd == "A":
        quit()