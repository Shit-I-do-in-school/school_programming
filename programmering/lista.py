#uppgift 7

x = int(input("Tal: "))
lista = []
lista.append(x)
y = x
for i in range(1,10):
    x = x * y
    lista.append(x)

print(lista)
print("Medelvärdet är:", round(sum(lista)/len(lista),2))
