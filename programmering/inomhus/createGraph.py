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
    for i in range(1, len(rooms)):
        startRoomLevel = int(rooms["omr"+str(i)].split(",")[0])
        startRoom = list(rooms["omr"+str(i)].split(",")[1])
        for j in range(2, len(rooms)):
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
    convertedCost = []
    visitedRooms = ["omr1"]
    for count in range(1,len(rooms)):
        fromRoom = rooms["omr"+str(count)].split(",")

        #get adjacent rooms
        for i in rooms:
            x = rooms[i].split(",")[1]
            for j in x:
                if j in fromRoom[1] and not i in visitedRooms:
                    adjacentRooms.append(i)

        #calculate cost
        for room in adjacentRooms:
            nextRoom = rooms[room].split(",")
            cost = int(nextRoom[0]) - int(fromRoom[0])
            convertedCost.append("omr"+str(count) + " " + str(cost))#try to add to graph somehow

        graph["omr" + str(count)] = convertedCost

    print_graph(graph)

def run():
    ''''
    n = int(input("Ange N: "))
    if not n >= 3 and not n <= 15:
        print("N är utanför gränsen")
        quit()


    rooms = {}
    for i in range(1, n+1):
        v = input(f"Område {i} våning --> ")
        t = input(f"Område {i} trappan --> ").upper()
        rooms["omr"+str(i)] = v + "," + t
    '''
    rooms = {
        "omr1": "1,AB",
        "omr2": "4,DE",
        "omr3": "1,CEF",
        "omr4": "3,AD",
        "omr5": "2,E",
        "omr6": "2,D",
        "omr7": "2,BC",
        "omr8": "3,F",
    }

    for j in range(1, len(rooms)):
        graph["omr"+str(j)] = {}
    print(graph)
    convert(rooms)

if __name__ == "__main__":
    run()