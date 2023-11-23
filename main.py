<<<<<<< Updated upstream
list = ["1", "2", "3", "4", "5", "6"]
list.pop(2)
list.insert(2, "AA")
x = ""
for i in list: x+= i

print(x)
=======
x = 0
y = 0

if x == 0  and y == 0:
    try: x + 1
    except ValueError:
        False
    try: y + 1
    except: print("Invalid")
elif x == 1 and y ==1:
    try: x - 1
    finally: print("wtf")
elif x == 1 and y == 2:
    x -= 1
    y -= 1
>>>>>>> Stashed changes
