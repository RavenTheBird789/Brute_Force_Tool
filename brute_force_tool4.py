import os
import random
import time

pas = input("Enter password: ")

keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
        "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", 
        "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
        "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", 
        "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", 
        ";", ":", "'", '"', ",", "<", ".", ">", "/", "?", 
        "\\", "|", "`", "~", " "]

attempt_count = 0
pwg = ""

# helper to clear screen in a cross-platform way (optional)
def clear_screen():
    cmd = "cls" if os.name == "nt" else "clear"
    os.system(cmd)

# Try random guesses until we match (note: this may take a very long time)
while pwg != pas:
    pwg = "" # start a fresh candidate
    for _ in range(len(pas)):
        guessPass = random.choice(keys) # pick from any character on a keyboard
        pwg += guessPass # append so order is natural
    attempt_count += 1

    # show progress every 100 attempts to reduce spam
    if attempt_count % 100 == 0:
        clear_screen()
        print(f"Attempts: {attempt_count} Current guess: {pwg}")
        print("attacking... please wait!")
        time.sleep(0.05) # small pause so output is readable

print(f"Password is: {pwg} (found in {attempt_count} attempts)")