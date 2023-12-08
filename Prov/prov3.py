
def save(item):
    with open("savedList.txt", "w") as f:
        for word in item:
            f.write(word + "\n")


def load():
    tempList = []
    with open("savedList.txt", "r") as f:
        for line in f:
            for word in line.split():
                tempList.append(word)
    return tempList


myList = load()
print(myList)
while 1:
    text = input("Skriv in nytt ord eller 'A' för att avsluta: ")
    try:
        pos = int(text)
        print(myList[pos-1])
    except IndexError:
        print("Positionen finns inte")
    except ValueError:
        if text.lower() != "a":
            myList.append(text)
            print(myList)
        else:
            print(myList)
            save(myList)
            break