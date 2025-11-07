import os
import random

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

pwg = ""
while(pwg!=pas):
    pwg=""
    for i in range(len(pas)):
        guessPass = random.choice(keys);
        pwg = str(guessPass)+str(pwg)
        print(pwg);
        print("attacking... please wait!")
        os.system("c1s")

print(f"Password is: {pwg}");
