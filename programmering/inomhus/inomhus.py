N = int(input("N = ")) #ange nummer för N

map = {}
    

def printmap():
    for item in map:
        print(item, "=", map[item])



if not N >= 3 and not N <= 15:
    print("N är utanför gränsen!")
    quit()

    
for i in range(1, N+1):
    map[str(i)+"v"] = int( input(f"område {  i  } våning --> "))
    map[str(i)+"t"]    =    input(f"område {  i  } trappa --> ")
map = {"1v": "2", "A": "2v", "1": "B"}

#posision = map["1v"], map["2v"]

a1 = int(input("vad är 1 + 4? "))

if a1 == 5:
    print("nice")
else:
    print("OMG YOU ARE RETARDED!!!!!")