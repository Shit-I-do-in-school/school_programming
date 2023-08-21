
i = int(input("siffran: "))

while i > 0:
    i = i-1
    if i < 3:
        print(f"warning siffran närmar sig noll: {i}")
    else:
        print(f"siffran är: {i}")