Cutelist = [1, 2, 3, 5, 5, 6, 1, 8, 9, 7, 2, 1]

def rep(i):
    for x in range(len(i)):
        if i[x]%2 == 0:
            i[x] = 0
    return i


print("Listan innan ändrigar", Cutelist)
WoW = rep(Cutelist)
print("listan efter ändring", WoW)