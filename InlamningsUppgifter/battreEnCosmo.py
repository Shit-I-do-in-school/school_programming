import time

braille = [
    " .* \n ** \n .. ",  # zero
    " *. \n .. \n .. ",  # one
    " *. \n *. \n .. ",  # two
    " ** \n .. \n .. ",  # three
    " ** \n .* \n .. ",  # four
    " *. \n .* \n .. ",  # five
    " ** \n *. \n .. ",  # six
    " ** \n ** \n .. ",  # seven
    " *. \n ** \n .. ",  # eight
    " .* \n *. \n .. ",   # nine
    " *. .* \n .. ** \n .. .. ",#ten
    " *. *. \n .. .. \n .. .. ",#elevn
    " *. *. \n .. *. \n .. .. ",#twele
    " *. ** \n .. .. \n .. .. ",#threde
    " *. ** \n .. .* \n .. .. ",#fourthe
    " *. *. \n .. .* \n .. .. ",#fig
    " *. ** \n .. *. \n .. .. ",#six
    " *. ** \n .. ** \n .. .. ",#sev
    " *. *. \n .. ** \n .. .. ",#eight
]

try:
    a,b = int(input("Tal ett: ")), int(input("Tal två: "))
    t1 = time.time()
    time.sleep(0.01) 
except:
    print("Det är inget tal :(")
    quit()

if a > 0 and a < 10 and b > 0 and b < 10:
    c = a+b
    print(braille[a])
    print("+")
    print(braille[b])
    print("=")
    print(braille[c])

    t2 = time.time()
    print("time = ", t2-t1)