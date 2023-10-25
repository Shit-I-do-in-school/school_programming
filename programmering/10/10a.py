def findvolume(length=1, width=1, depth=1):
    
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    print(length * width * depth) #skriver ut matte, volymen
    return length * width * depth # returnerar matte (om dubehöver det, spara i nån global var)

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)