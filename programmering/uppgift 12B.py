
def do(text, word1, word2):
    text = text.lower().replace(word1, word2)
    return text

print(do(input("text: "), input("Ord at byta: "), input("Nya ord: ")))