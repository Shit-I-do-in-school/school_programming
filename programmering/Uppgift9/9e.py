lista = []

for i in range(10):
    lista.append(input("Ord: "))

while 1:
    print(lista)
    place = int(input("Plats i listan (börjar från ett, noll får loopen att stanna): "))
    if place == 0: break
    new_word = input("Ny ord: ")
    lista[place-1] = new_word