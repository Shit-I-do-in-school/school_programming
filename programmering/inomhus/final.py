
graph = {}
travel_cost = 0
min_trav = {}

def print_graph(graph):# prints graph variable in a nice way
    for i in range(1,len(graph)+1):
        item = str(graph["omr"+str(i)])
        print("omr"+str(i) + ": " + item)


def convert(rooms):# maps out path cost
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

# rooms = {
#     "omr1": "1,AB",
#     "omr2": "4,DE",
#     "omr3": "1,CEF",
#     "omr4": "3,AD",
#     "omr5": "2,E",
#     "omr6": "2,D",
#     "omr7": "2,BC",
#     "omr8": "3,F",
#     "omr9": "4,A"
# }

# rooms={
#     "omr1":"2,A",
#     "omr2": "100,A",
#     "omr3": "3,A"
# }

for j in range(1, len(rooms) + 1):# init dict names
    graph["omr" + str(j)] = {}
map = convert(rooms)


def pathfind(next_platform, travel_path, paths, chain=0, selfCalled=False, carriedPlatforms=[]):
    if not selfCalled:
        for av_platform in paths:
            if next_platform in map[av_platform]:
                min_trav[travel_path] = paths[av_platform] + map[av_platform][next_platform]
            else:
                carriedPlatforms.append(av_platform)
                pathfind(next_platform, travel_path, paths, chain=chain, selfCalled=True, carriedPlatforms=carriedPlatforms)
    else: #is self called
        if chain < 14:
            chain += 1
            for previus_platforms in carriedPlatforms:
                for platforms in map[previus_platforms]:
                    if next_platform in map[platforms]:
                        min_trav[travel_path] = paths[platforms] + map[platforms][next_platform]
                    else:
                        carriedPlatforms.append(platforms)
                        pathfind(next_platform, travel_path, paths, chain=chain, selfCalled=True, carriedPlatforms=carriedPlatforms)
        else: print("Chain to long")


for platform in map:
    next_platform = f"omr{int(platform[-1:]) + 1}"
    travel_path = f"{platform}-omr{int(platform[-1:]) + 1}"
    paths = map[platform]

    if next_platform in paths:
        min_trav[travel_path] = paths[next_platform]

    else:
        for av_platform in map[platform]:
            if next_platform in map[av_platform]:
                min_trav[travel_path] = paths[av_platform] + map[av_platform][next_platform]

            else:
                for av2_platform in map[av_platform]:
                    if next_platform in map[av2_platform]:
                        travel_cost = paths[av_platform] + map[av2_platform][next_platform] + map[av_platform][av2_platform]

                        #calculate final cost and steps
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