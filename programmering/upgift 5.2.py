i = int(input("hur många gånger ska jag säga hej?"))
p = 1

while p < i + 1:
    print("hej")
    p += 1
    if p == i + 1:
        break