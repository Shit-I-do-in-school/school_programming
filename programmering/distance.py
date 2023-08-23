#bensin pris
Bensinpris = 20
#förbrukning per km.
förbrukning = 1.5

#hur långt åker du?
distans = float(input("Hur långt ska du åka?"))

#räkna ut hur mycket bensin du använde under resan.
användning = distans * förbrukning

#räkna ut hur mycket resan kostar.
kostnad = distans * användning

#printa ut svaren.
print("Du åkte ", distans, "km"," förbrukade ", användning, "L"," Det kostade ", kostnad, "kr")