def varfor(text, word1, word2):
    text = text.lower().replace(word1, word2)
    return text
    
    
print(varfor(input("Skriv din text: "), input("Byt ut ord "), input("skriv nya ord ")))