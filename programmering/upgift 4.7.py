lista = []
x = int(input("Din tal: "))
for i in range(1,x+1):
   if i%3 == 0 or i%7 == 0:
       lista.append(i)

print("Delbara tal är: ", lista)