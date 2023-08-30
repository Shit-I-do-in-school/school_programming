lista = []

while True:
    x = int(input("Din tal: "))

    if x < 0:
        print("Ogiltigt tal. Försök igen.")
        continue

    elif x > 0:
        for i in range(1, x + 1):
            if i % 3 == 0 and i % 7 == 0:
                lista.append(i)
                
    if lista:
        print("Tal som är jämnt delbara med både 3 och 7: ", lista)
    else:
        print("Inga tal hittades som är delbara med både 3 och 7: ",)

    break
