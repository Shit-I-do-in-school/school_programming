lista = [1,5,9,4,7,9,4,8,5,0,6]

def replace(i):
    for x in range(len(i)):
        if i[x]%2 == 0:
            i[x] = 0
    return i

print("Lista innan: ", lista)
a = replace(lista)
print("Lista efter: ", lista)