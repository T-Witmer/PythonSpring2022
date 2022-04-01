# Troy Witmer

import re

text = open("words.txt", "r")
text = text.read()

def catdog(text):
    cat = r"[C|c][A|a][T|t]"
    dog = r"[D|d][O|o][G|g]"
    catoutput = re.findall(cat,text)
    dogoutput = re.findall(dog,text)
    output = len(catoutput) + len(dogoutput)

    return output

print(catdog(text))
