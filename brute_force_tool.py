import os
from random import randint

pas = input("Enter password: ")

keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

pwg = ""
while(pwg!=pas):
    pwg=""
    for i in range(len(pas)):
        guessPass = keys[randint(0, 6)]
        pwg = str(guessPass)+str(pwg)
        print(pwg)
        print("attacking... please wait!")
        os.system("c1s")

print(f"Password is: {pwg}");