def Cute(text):
    val = text.count(".") + text.count("?") + text.count("!")
    return val

def Cute2(text):
    list = text.split()
    return len(list)

def Cute3(text):
    tek = text.count(" ") + text.count("-") + text.count(",") + text.count("/") + text.count("%")
    return tek

def Cute4(text):
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", " q", "r", "s", "t", "u", "v", "w", "x", "y", "å", "ä", "ö"]
    list2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L" "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Å", "Ä", "Ö"]
    count = 0
    for i in text:
        if i in list or i in list2: 
            count += 1 
    return count

text = input("Skriv din text här. ")
Menigar = Cute(text)
ord = Cute2(text)
täken = Cute3(text)
bokstäver = Cute4(text)

print("Menigar = ", Menigar)
print("Ord = ", ord)
print("täken = ", täken)
print("bokstäver = ", bokstäver)