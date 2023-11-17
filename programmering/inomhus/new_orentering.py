n = int(input("Ange N: "))
if not n >= 3 and not n <= 15:
    print("N är utanför gränsen")
    quit()


roomss = {}
visited_rooms = {}

#example rooms
rooms = {
    "omr1": "1,AB",
    "omr2": "4,BC",
    "omr3": "5,CE",
    "omr4": "10,DE"
}

'''''
for i in range(1, n+1):
    v = input(f"Område {i} våning --> ")
    t = input(f"Område {i} trappan --> ").upper()
    rooms["omr"+str(i)] = v + "," + t
'''''


visited = 0
x = 0
visited_rooms[0] = rooms["omr1"]
while visited < len(rooms):
    x += 1
    #explore
    current_room = rooms["omr1"]
    choices = rooms["omr"+str(x)].split(",")[1]#example look: AB

