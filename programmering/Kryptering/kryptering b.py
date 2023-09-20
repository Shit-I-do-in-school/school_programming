def isSV(char):
    return char.isalpha() and (char.islower() or char.isupper()) and char not in ('Å', 'Ö', 'Ä', 'å', 'ö', 'ä')

def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if isSV(char):
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if isSV(char):
            if char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char

    return result

state = input("Kryptera eller dekryptera? k/d: ")
key = int(input("Nyckeln (tal mellan 1 och 24): "))
text = input("Ordet att modifera: ")

if state == "k":
    newWord = encrypt(text,key)
    print("Färdig ord: ", newWord)
elif state == "d":
    newWord = decrypt(text,key)
    print("Färdig ord: ", newWord)
else:
    print("Fel bokstav")