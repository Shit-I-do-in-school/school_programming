import sys  # Import the sys module

# Skapa en tom lista för att lagra orden
Cutelist = []

# Loop för att mata in 10 ord
for i in range(10):
    Cutelist.append(input("skriv ord: "))
    
# Skriv ut orden med en loop
for x in Cutelist:
  print(x)

while True:
    print("listan just nu:", Cutelist)
    I = int(input("Ange indexet för ordet du vill byta ut 0-9: "))

    if I < 0 or I >= len(Cutelist):
        print("Ogiltigt index. Försök igen.")
        continue  # Skip the rest of the loop and start over
    
    O = input("Mata in det nya ordet: ")
    if O == "0":  # Use "0" (a string) for comparison
        for x in Cutelist:
            print(x)
        print("Det här är din lista")
        sys.exit()  # Exit the program
    
    else:
        Cutelist[I] = O
        svar = input("Vill du fortsätta byta ord? (ja/nej): ")
        if svar.lower() != "ja":
            for x in Cutelist:
                print(x)
            break
    
print("Det här är din lista")
