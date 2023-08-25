#bensin pris
bensinPris = 20
#förbrukning per km.
förbrukning = 1.5

#hur långt åker du?
distans = float(input("Hur långt ska du åka i km? "))

#räkna ut hur mycket bensin du använde under resan.
bränsle = distans*förbrukning

#räkna ut hur mycket resan kostar.
kostnad = distans*bensinPris

#printa ut svaren.
print(f"Du använde {bränsle} bensin och kostade {kostnad}kr")