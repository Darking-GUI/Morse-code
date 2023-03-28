

def emoji(message):
    words = message.split(" ")


    emojis = {
        " " : " ",
        "0" : "_____",
        "1" : ".____",
        "2" : "..___",
        "3" : "...__",
        "4" : "...._",
        "5" : ".....",
        "6" : "_....",
        "7" : "__...",
        "8" : "___..",
        "9" : "____.",
        "." : "___.",
        "_" : "..__",
        "-" : "____",
        "m" : "__",
        "i" : "..",
        "a" : "._",
        "A" : "._",
        "I" : "..",
        "t" : "_",
        "e" : ".",
        "n" : "_.",
        "o" : "___",
        "g" : "__.",
        "k" : "_._",
        "d" : "_..",
        "w" : ".__",
        "r" : "._.",
        "u" : ".._",
        "s" : "...",
        "q" : "__._",
        "z" : "__..",
        "y" : "_.__",
        "c" : "_._.",
        "x" : "_.._",
        "b" : "_...",
        "j" : ".___",
        "p" : ".__.",
        "l" : "._..",
        "f" : ".._.",
        "v" : "..._",
        "h" : "____",
        "M" : "__",
        "T" : "_",
        "E" : ".",
        "N" : "_.",
        "O" : "___",
        "G" : "__.",
        "K" : "_._",
        "D" : "_..",
        "W" : ".__",
        "R" : "._.",
        "U" : ".._",
        "S" : "...",
        "Q" : "__._",
        "Z" : "__..",
        "Y" : "_.__",
        "C" : "_._.",
        "X" : "_.._",
        "B" : "_...",
        "J" : ".___",
        "P" : ".__.",
        "L" : "._..",
        "F" : ".._.",
        "V" : "..._",
        "H" : "____",
    }

    output = ""

    for word in words :
        output += emojis.get(word , "ERR") + " "
    return output     

def zeta(message):
    words = message.split(" ")


    emojis = {
        " " : " ",
        "0" : "_____",
        "1" : ".____",
        "2" : "..___",
        "3" : "...__",
        "4" : "...._",
        "5" : ".....",
        "6" : "_....",
        "7" : "__...",
        "8" : "___..",
        "9" : "____.",
        "." : "___.",
        "_" : "..__",
        "-" : "____",
        "m" : "__",
        "t" : "_",
        "e" : ".",
        "n" : "_.",
        "o" : "___",
        "g" : "__.",
        "k" : "_._",
        "d" : "_..",
        "w" : ".__",
        "r" : "._.",
        "u" : ".._",
        "s" : "...",
        "q" : "__._",
        "z" : "__..",
        "y" : "_.__",
        "c" : "_._.",
        "x" : "_.._",
        "b" : "_...",
        "j" : ".___",
        "p" : ".__.",
        "l" : "._..",
        "f" : ".._.",
        "v" : "..._",
        "h" : "____",
        "i" : "..",
        "a" : "._",
    }
    
    sawped = {v : k for k, v in emojis.items()}

    output = ""

    for word in words :
        output += sawped.get(word , "ERR") + " "
    return output     




main_input = input(f"""Choose :
        
*if you wanna translate ==> Enter 1
*if you wanna close the program ==> Enter 2
*if you wanna trascript ==> Enter anything you want
----------------------------
for translating don't use this structure :
hey it is me.

Write with addintional space like this :
h e y i t i s m e .
----------------------------


> """)

if main_input == "1" :
    print(emoji(input("> ")))
elif main_input == "2" :
    print(zeta(input("> ")))
else:
    print("ok")