<<<<<<< HEAD
list = []

def cipher_decrypt_lower(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if 1:

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og
            if not decrypted in list:
                list.append(decrypted)

        else:

            decrypted += c

    return decrypted


cryptic_text = input("Skriv det encryptade text här: ")

for i in range(0, 100000):

    plain_text = cipher_decrypt_lower(cryptic_text, i)

    print("For key {}, decrypted text: {}".format(i, plain_text))

print(len(list))
x = 0
with open("possible.txt", "w") as f:
    for i in range(0,len(list)):
        f.write(list[x] + "\n")
        x +=1

=======
list = []

def cipher_decrypt_lower(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if 1:

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og
            if not decrypted in list:
                list.append(decrypted)

        else:

            decrypted += c

    return decrypted


cryptic_text = input("Skriv det encryptade text här: ")

for i in range(0, 100000):

    plain_text = cipher_decrypt_lower(cryptic_text, i)

    print("For key {}, decrypted text: {}".format(i, plain_text))

print(len(list))
x = 0
with open("possible.txt", "w") as f:
    for i in range(0,len(list)):
        f.write(list[x] + "\n")
        x +=1

>>>>>>> 7822b087e88dcd91deaf64df3c902a33fd6707f9
#1121222919