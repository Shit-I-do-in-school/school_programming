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

    
    O = input("Mata in det nya ordet: ")
    if O == 0:
            print(x)
            print("Det här är din lista")
#SLUTA DET HÄR FUCKING PROGRAMET SNÄLLA JAG ÅRKAR INTE GÖRA DET HÄR T.T
            
    elif O != 0:
        Cutelist[I] = O
    
        svar = input("Vill du fortsätta byta ord? (ja/nej): ")
        if svar.lower() != "ja":
            for x in Cutelist:
                print(x)
            break
    
print("Det här är din lista")
    
