import string

def isSV(char):
    return char.isalpha() and (char.islower() or char.isupper()) and char not in ('Å', 'Ö', 'Ä', 'å', 'ö', 'ä',)

# Define the character set to include Swedish letters
character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " "+ string.punctuation + 'ÅÄÖåäö'

print("Extended character set:\n", character_set)

def encrypt(text, keys):

    result = ""
    key_index = 0  # Initialize the key_index to 0

    for c in text:

        if c in character_set:
            char_index = character_set.index(c)
            key = keys[key_index % len(keys)]  # Use the next key in the list
            c_new = character_set[(char_index + key) % len(character_set)]
            key_index += 1  # Move to the next key

        else:
            # If it's not in the character_set, leave it unchanged
            c_new = c

        result += c_new

    return result


def decrypt(text, keys):

    result = ""
    key_index = 0  # Initialize the key_index to 0

    for c in text:

        if c in character_set:
            char_index = character_set.index(c)
            key = keys[key_index % len(keys)]  # Use the next key in the list
            c_og = character_set[(char_index - key) % len(character_set)]
            key_index += 1  # Move to the next key

        else:
            # If it's not in the character_set, leave it unchanged
            c_og = c

        result += c_og

    return result

state = input("Kryptera eller dekryptera? k/d: ")
key_str = input("Ange nycklar separerade med mellanslag: ")
keys = [int(key) for key in key_str.split()]  # Split the input string into a list of keys
text = input("Ordet att modifera: ")

if state == "k":
    newWord = encrypt(text, keys)
    print("Färdig ord: ", newWord)
elif state == "d":
    newWord = decrypt(text, keys)
    print("Färdig ord: ", newWord)
else:
    print("Fel bokstav")
