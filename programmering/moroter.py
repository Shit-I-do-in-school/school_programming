<<<<<<< HEAD
moroter = 40
tor = int(input("tor: "))
mor = int(input("mor: "))

tor_eaten = 0
mor_eaten = 0
tick = 1

while not tor_eaten + mor_eaten >= moroter or tor_eaten + mor_eaten < moroter:
    currect_carrot = tor_eaten + mor_eaten
    a = tick % tor
    b = tick % mor
    #print("carrot: ", currect_carrot)
    #print("t: ", a)
    #print("m: ", b)
    if currect_carrot == 39:
        if a == 1 and b == 1:
            break
    if a == 0:
        tor_eaten +=1
    if b == 0:
        mor_eaten +=1
    tick += 1

print("TOTAL tor: ", tor_eaten)
print("TOTAL mor: ", mor_eaten)
=======
moroter = 40
tor = int(input("tor: "))
mor = int(input("mor: "))

tor_eaten = 0
mor_eaten = 0
tick = 1

while not tor_eaten + mor_eaten >= moroter or tor_eaten + mor_eaten < moroter:
    currect_carrot = tor_eaten + mor_eaten
    a = tick % tor
    b = tick % mor
    #print("carrot: ", currect_carrot)
    #print("t: ", a)
    #print("m: ", b)
    if currect_carrot == 39:
        if a == 1 and b == 1:
            break
    if a == 0:
        tor_eaten +=1
    if b == 0:
        mor_eaten +=1
    tick += 1

print("TOTAL tor: ", tor_eaten)
print("TOTAL mor: ", mor_eaten)
>>>>>>> 7822b087e88dcd91deaf64df3c902a33fd6707f9
