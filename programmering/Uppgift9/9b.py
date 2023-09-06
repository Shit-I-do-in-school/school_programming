lista = []

while 1:
    tal = int(input("Tal: "))
    if tal == 0: break
    lista.append(tal)#om "tal" är noll så skipas den del och talen sparas inte

print("Medelvärdet:", sum(lista) / len(lista))