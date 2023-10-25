x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

def Hejsvejs(x, y, z):
    if x > y and x > z: return x
    if y > x and y > z: return y
    if z > y and z > y: return z
    
OMG = Hejsvejs(x, y, z)

print(OMG)