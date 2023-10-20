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
        #this is like black magic p.s this should not work but does!
        if a == 1 and b == 1:
            break
    if a == 0:
        tor_eaten +=1
    if b == 0:
        mor_eaten +=1
    tick += 1
    
print("TOTAL tor: ", tor_eaten)
print("TOTAL mor: ", mor_eaten)