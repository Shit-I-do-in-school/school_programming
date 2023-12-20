
graph = {}
travel_cost = 0
min_travel = {}

def print_graph(graph):# prints graph variable in a nice way
    for i in range(1,len(graph)+1):
        item = str(graph["omr"+str(i)])
        print("omr"+str(i) + ": " + item)


def convert(rooms):# maps out path cost
    adjacentRooms = []
    for count in range(1,len(rooms)+1):#loop for each omr
        adjacentRooms = []
        fromRoom = rooms["omr"+str(count)].split(",")

        #get adjacent rooms
        for i in range(1, len(rooms)+1):#loop for count rooms
            x = rooms["omr"+str(i)].split(",")# variable is --> ie. AB
            for j in x[1]:
                if j in fromRoom[1]:# if stairs match then add to list
                    adjacentRooms.append(i)

        #calculate cost
        for level in adjacentRooms:
            nextRoom = rooms["omr"+str(level)].split(",")
            cost = abs(int(nextRoom[0]) - int(fromRoom[0]))#calculate cost
            if "omr"+str(count) != "omr"+str(level):# check if adjacent room is origin room
                graph["omr"+str(count)]["omr"+str(level)] = cost #add everything to graph

    print_graph(graph)#print graph in a readable style
    return graph



# n = int(input("Ange N: "))
# if not n >= 3 and not n <= 15:
#     print("N är utanför gränsen")
#     quit()
#
#
# rooms = {}
# for i in range(1, n+1):
#     v = input(f"Område {i} våning --> ")
#     t = input(f"Område {i} trappan --> ").upper()
#     rooms["omr"+str(i)] = v + "," + t

# rooms = {#answer is 24
#     "omr1": "1,AB",
#     "omr2": "4,DE",
#     "omr3": "1,CEF",
#     "omr4": "3,AD",
#     "omr5": "2,E",
#     "omr6": "2,D",
#     "omr7": "2,BC",
#     "omr8": "3,F"
# }

rooms = {
    "omr1": "2,A",
    "omr2": "4,ABDE",
    "omr3": "2,F",
    "omr4": "3,EF",
    "omr5": "7,D",
    "omr6": "6,BC",
    "omr7": "1,A",
    "omr8": "8,C",
    "omr9": "8,D",
}

# rooms = {#answer is 15
#     "omr1": "1,A",
#     "omr2": "5,B",
#     "omr3": "3,BCD",
#     "omr4": "2,C",
#     "omr5": "1,D",
#     "omr6": "5,A",
#     "omr7": "4,AB"
# }

# rooms={#answer is 195
#     "omr1":"2,A",
#     "omr2": "100,A",
#     "omr3": "3,A"
# }

for j in range(1, len(rooms) + 1):# create graph
    graph["omr" + str(j)] = {}
map = convert(rooms)#insert variables into graph


for platform in map:
    next_platform = f"omr{int(platform[-1:]) + 1}"
    travel_path = f"{platform}-omr{int(platform[-1:]) + 1}"#create easy to read path

    if next_platform in map[platform]:#if targer room is edjacent
        min_travel[travel_path] = map[platform][next_platform]#add path to variable

    else:#loop for extra path to find target room
        for av_platform in map[platform]:#loop for available rooms
            if next_platform in map[av_platform]:#if targer room is found
                min_travel[travel_path] = map[platform][av_platform] + map[av_platform][next_platform]#add path to variable

            else:
                for av2_platform in map[av_platform]:#loop by looking 2 rooms ahead
                    if next_platform in map[av2_platform]:
                        travel_cost = map[platform][av_platform] + map[av2_platform][next_platform] + map[av_platform][av2_platform]#add path to variable

                        #check which is shorter
                        if travel_path in min_travel:#if same path exists
                            if travel_cost < min_travel[travel_path]:#pick the shorter path
                                min_travel[travel_path] = travel_cost
                        else:
                            min_travel[travel_path] = travel_cost


total_travel = 0
for val in min_travel:#calculate path cost
    total_travel += min_travel[val]

print(min_travel)
print(total_travel)

