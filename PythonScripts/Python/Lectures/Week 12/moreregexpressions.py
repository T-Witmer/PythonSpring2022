#Troy Witmer

#automatetheboringsutff.com

import re

vowels = r"[AEIOUaeiou]"
notvowel = r"[^AEIOUaeiou]" #use carrot to indicate not* this

word = r"\w" #letter number and underscores
digit = r"\d" #digits
whitespace = r"\s" #space, tabs, anything with white space
notword = r"\W"
notdigit = r"\D"
notwhitespace = r"\S"

#hahahahaha

halol = r"(ha){1,5}|lol" #parenthesis to group

kleanstar = r"ab*a" # at least zero b's
plus = r"ab+a" # at least one b
question = r"ab?a" #for zero to one

# Given a file with phone numbers write a new file with those numbers blank

def redactphone(filein, fileout):
    data = open(filein,"r")
    text = data.read()
    phonenumber = r"(*\d{3})*-* *\d{3}-*\d{4}"
    output = re.sub(phonenumber, "REDACTED", filein)
    write = open(fileout, "w")
    write.write(output)
    write.close()

redactphone("phonenumber.txt", "output.txt")

