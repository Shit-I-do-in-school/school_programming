text = input("vad vill du att den ska skriva?")
i = int(input("hur många gånger ska jag säga din text?"))
p = 1

while p < i + 1:
    print(text)
    p += 1
    if p == i + 1:
        break