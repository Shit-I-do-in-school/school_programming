n = int(input("Ange N: "))#antal område

room = {}

if not n >= 3 and not n <= 15:
    print("N är utanför gränsen")
    quit()

for i in range(1, n+1):
    v = input(f"Område {i} våning --> ")
    t = input(f"Område {i} trappan --> ").upper()
    room["room"+str(i)] = f"{v},{t}"
print(room)

position = room["room1"].split(",")
visited = [room["room1"]]
choices = []


def addChoices():
    for item in room:#add available room choices to choices list
        x = room[item].split(",")
        print("p: ", position[1])
        print("x: ", x[1])
        if position[1] in x[1]:
            choices.append(room[item].split(","))
    print(choices)

def removeVisited():
    for i in range(len(choices)):#remove visited rooms from available choices
        try:
            x = visited[i].split(",")
            if x[1] in choices[i]:
                print("removing: ", choices[i])
                choices.remove(choices[i])
        except: pass
    print(choices)


while len(visited) != len(room):
    addChoices()
    removeVisited()
