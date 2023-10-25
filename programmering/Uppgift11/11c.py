def hejsvejs(x,y,z):
    if x > y and x > z: return x
    if y > x and y > z: return y
    if z > y and z > x: return z

storsta = hejsvejs(int(input("x: ")),int(input("y: ")),int(input("z: ")))

print(storsta)