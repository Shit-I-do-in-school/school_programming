import os

def cmdGet():
    print("Öppna en textfil --> o")
    print("Skapa en ny textfil --> n")
    print("Avsluta program --> a")
    return input("Command: ")

def editFile(filename):
    print("Lägg till en rad i textfilen --> l")
    print("Skriv ut text --> s")
    print("Radera filen --> r")
    print("Avsluta --> a")
    cmd = input("Command: ")
    with open(filename, "w") as f:
        if cmd == "l": f.write(input("text at lägga till:\n"))
        elif cmd == "s": print(f.read())
        elif cmd == "r": os.remove(filename)
        elif cmd == "a": quit()

def skapa():
    file = input("Skriv namn och path på filen du vill skapa: ")
    if not ".txt" in file: file = file+".txt"

    try: f = open(file, 'x')
    except FileExistsError: print("Filen finns redan")
    except Exception as e: print("Error: ", e)
    else: print("Filen skapats")

    if input("Vill du redigera filen nu? j/n ") == "j": editFile(file)

while 1:
    cmd = cmdGet()
    if cmd == "o": editFile(input("Namn och path till textfilen: "))
    elif cmd == "n": skapa()
    elif cmd == "a": quit()
    else: print("Okänd kommando")