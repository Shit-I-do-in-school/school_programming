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
    for i in range(1,len(graph)+1):
        item = str(graph["omr"+str(i)])
        print("omr"+str(i) + ": " + item)

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
    return graph



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
        "omr8": "3,F"
    }

    for j in range(1, len(rooms)+1):
        graph["omr"+str(j)] = {}

    distances = convert(rooms)

    travel_cost = 0
    min_trav = {}

    # target_platform = f"omr2"
    # for path_option in distances['omr1']:
    #     if target_platform in path_option:

    n = len(distances)
    for platform in distances:
        print(platform)
        next_platform = f"omr{int(platform[-1:]) + 1}"
        travel_path = f"{platform}-omr{int(platform[-1:]) + 1}"

        if next_platform in distances[platform]:
            min_trav[travel_path] = distances[platform][next_platform]

        else:
            for av_platform in distances[platform]:
                if next_platform in distances[av_platform]:
                    min_trav[travel_path] = distances[platform][av_platform] + distances[av_platform][next_platform]

                else:
                    for av2_platform in distances[av_platform]:
                        if next_platform in distances[av2_platform]:

                            travel_cost = distances[platform][av_platform] + distances[av2_platform][
                                next_platform] + distances[av_platform][av2_platform]

                            if travel_path in min_trav:
                                if travel_cost < min_trav[travel_path]:
                                    min_trav[travel_path] = travel_cost
                            else:
                                min_trav[travel_path] = travel_cost

    total_travel = 0
    for val in min_trav:
        total_travel += min_trav[val]


    print(min_trav)
    print(total_travel)

if __name__ == "__main__":
    run()