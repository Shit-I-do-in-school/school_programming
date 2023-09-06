lista = []

for i in range(10):
    lista.append(input("Ord: "))

while 1:
    print(lista)
    place = int(input("Plats i listan (börjar från noll): "))
    new_word = input("Ny ord: ")
    lista[place] = new_word