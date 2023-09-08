menu = ["mat1, mat2, mat3, mat4"]#orkar inte tänka på meny
def fun(i):
    x = int(i)
    bord = 0
    while x > 0:
        x = x-4
        bord = bord+1
    print("antal bord 4 personer per bord: ", bord)

    print("meny:")
    for y in menu: print(y)
    return int(i)*149

pris = fun(input("Antal besökare: "))

print("Buffe pris: ", pris)