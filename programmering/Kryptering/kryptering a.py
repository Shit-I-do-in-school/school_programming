def kryptera(text,key):
    result = ""
 
    
    for i in range(len(text)):
        char = text[i]
 
        
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
 
        
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
 
    return result

def dekryptera(text, key):
    result = ""
 
    
    for i in range(len(text)):
        char = text[i]
 
        
        if (char.isupper()):
            result += chr((ord(char) - key - 65) % 26 + 65)
 
        
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
 
    return result

other = input("Skall ni krypera, K, eller dekryptera, D ")
text = input("Skriv ditt ord du vill krypera eller dekrypera! ")
key = int(input("Skriv in nyckeln d.v.s ett tal mellan 1 och 24! "))

if other == "K":
    newtext = kryptera(text, key)
    print("Ditt ord", newtext)
    
elif other == "D":
    newtext = dekryptera(text, key)
    print("Ditt ord", newtext)