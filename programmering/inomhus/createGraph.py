'''
TODO:
1. make a remover for last item in graph dict (remove the extra added item for looping)
2. fix counting all rooms on same stairs
3. convert omr1 to letters

'''


'''''
GOAL:

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
    'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
    'E': {'C': 5, 'D': 11, 'F': 1},
    'F': {'D': 22, 'E': 1}
}

rooms = {
    "omr1": "1,AB",
    "omr2": "4,BC",
    "omr3": "5,CE",
    "omr4": "10,DE"
}
'''''
graph = {}

def print_graph(graph):
    for i in range(1,len(graph)):
        item = str(graph["omr"+str(i)])
        print("omr"+str(i) + ": " + item)

def convert1(rooms):
    for i in range(1, len(rooms)+1):
        startRoomLevel = int(rooms["omr"+str(i)].split(",")[0])
        startRoom = list(rooms["omr"+str(i)].split(",")[1])
        for j in range(2, len(rooms)+2):
            try:
                tempLevel = int(rooms["omr" + str(j)].split(",")[0])
                tempStair = list(rooms["omr"+str(j)].split(",")[1])
            except: print("No Rooms Left")
            print("startRoomLevel: ", startRoomLevel)
            print("tempLevel: ", tempLevel)
            print("startRoom: ", startRoom)
            print("tempStair: ", tempStair)
            for k in tempStair:
                if k in startRoom:
                    diff = startRoomLevel-tempLevel

                    print(diff)


def convert(rooms):
    #variable init
    adjacentRooms = []
    for count in range(1,len(rooms)+1):
        adjacentRooms = []
        fromRoom = rooms["omr"+str(count)].split(",")

        #get adjacent rooms
        for i in range(1, len(rooms)+1):#loop for count rooms
            x = rooms["omr"+str(i)].split(",")# variable is --> ie. AB
            for j in x[1]:# brain damage here
                if j in fromRoom[1]:
                    adjacentRooms.append(i)

        #calculate cost
        for level in adjacentRooms:
            nextRoom = rooms["omr"+str(level)].split(",")
            cost = abs(int(nextRoom[0]) - int(fromRoom[0]))
            if "omr"+str(count) != "omr"+str(level):
                graph["omr"+str(count)]["omr"+str(level)] = cost #add everything to graph

    print_graph(graph)
    #return graph

def checkForFaults(graph):
    for item in graph:
        print(item)

def run():
    '''''
    n = int(input("Ange N: "))
    if not n >= 3 and not n <= 15:
        print("N är utanför gränsen")
        quit()


    rooms = {}
    for i in range(1, n+1):
        v = input(f"Område {i} våning --> ")
        t = input(f"Område {i} trappan --> ").upper()
        rooms["omr"+str(i)] = v + "," + t
    '''''
    rooms = {
        "omr1": "1,AB",
        "omr2": "4,DE",
        "omr3": "1,CEF",
        "omr4": "3,AD",
        "omr5": "2,E",
        "omr6": "2,D",
        "omr7": "2,BC",
        "omr8": "3,F",
        "omr9": "1,ZZZ"
    }

    for j in range(1, len(rooms)+1):
        graph["omr"+str(j)] = {}
    convert(rooms)
    #a = convert(rooms)

    #checkForFaults(a)

if __name__ == "__main__":
    run()