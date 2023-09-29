import string

def isSV(char):
    return char.isalpha() and (char.islower() or char.isupper()) and char not in ('Å', 'Ö', 'Ä', 'å', 'ö', 'ä',)

character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " "+ string.punctuation + 'ÅÄÖåäö'

def encrypt(text, keys):
    result = ""
    key_index = 0

    for c in text:
        if c in character_set:
            char_index = character_set.index(c)
            key = keys[key_index % len(keys)]
            c_new = character_set[(char_index + key) % len(character_set)]
            key_index += 1
        else:
            c_new = c
        result += c_new
    return result


def decrypt(text, keys):
    result = ""
    key_index = 0

    for c in text:
        if c in character_set:
            char_index = character_set.index(c)
            key = keys[key_index % len(keys)]
            c_og = character_set[(char_index - key) % len(character_set)]
            key_index += 1
        else:
            c_og = c
        result += c_og
    return result

state = input("Kryptera eller dekryptera? k/d: ")
key_str = input("Ange nycklar separerade med mellanslag: ")
keys = [int(key) for key in key_str.split()]
text = input("Ordet att modifera: ")

if state == "k":
    newWord = encrypt(text, keys)
    print("Färdig ord: ", newWord)
elif state == "d":
    newWord = decrypt(text, keys)
    print("Färdig ord: ", newWord)
else:
    print("Fel bokstav")

#1 22 9 7