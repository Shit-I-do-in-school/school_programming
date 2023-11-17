normal = input("Skriv in en text som skall översättas till Rövarspråk: ").lower()# ta in string och omvandla till små bokstäver
konsonanter = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","z","x"]#konsonanterna


def convert(text):#funktion till att översätta
    #fixa variabler
    letters = []
    pos = 0
    final = ""

    for letter in text: letters.append(letter)#konvertar inputen till list med varje bokstav och symbol som egen objekt

    for item in letters:#for varje objekt i listan
        if item in konsonanter:#om bokstaven är konsonant
            new_item = item + "o" + item#lägger till o och samma bokstav
            #byt ut bokstaven med nya bokstäver som är översättade
            letters.pop(pos)
            letters.insert(pos, new_item)
        pos += 1#den räknar position i listan letters

    for i in letters: final += i#omvandla listan letters till en string kallade final
    return final#returna stringet


print(convert(normal))#den gör funktionen convert och printar ut svaren direkt