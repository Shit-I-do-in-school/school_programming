# Skapa en tom lista för att lagra orden
Cutelist             =                  []

# Loop för att mata in 10 ord
for         i           in range        (10):
    Cutelist.       append(float(input     ("skriv tal: ")))
    
    
medelvarde               = sum        (Cutelist) / len            (Cutelist)


print   ("medelvardet av alla tal är: ",                    medelvarde                         )