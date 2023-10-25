def meningar(text):
    value = text.count(".") + text.count("?") + text.count("!")
    return value

def ord(text):
    list = text.split()
    return len(list)

def tecken(text):
    value = text.count(" ") + text.count(",") + text.count("-") + text.count("/") + text.count(".")
    return value

def bokstaver(text):
    listA = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
    listB = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]
    count = 0
    for i in text:
        if i in listA or i in listB:
          count += 1
    return count

text = input("Skriv in några meningar: ")

antal_meningar = meningar(text)
antal_ord = ord(text)
antal_tecken = tecken(text)
antal_bokst = bokstaver(text)

print("Meningar:", antal_meningar)
print("Ord:", antal_ord)
print("Tecken:", antal_tecken)
print("Bokst:", antal_bokst)