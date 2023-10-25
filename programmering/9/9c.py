# Skapa en tom lista för att lagra orden
Cutelist = []

# Loop för att mata in 10 ord
for i in range(10):
    Cutelist.append(int(input("skriv tal: ")))
    

Cutelist.sort()

median = len(Cutelist)/2


print("medianen av alla tal är: ", Cutelist[int(median)])