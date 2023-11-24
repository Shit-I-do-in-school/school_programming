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

def convert(rooms):
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
        "omr2": "4,BC",
        "omr3": "3,C",
        "omr4": "10,DE"
    }

    for j in range(1, len(rooms)):
        graph["omr"+str(j)] = ""
    print(graph)
    convert(rooms)

if __name__ == "__main__":
    run()