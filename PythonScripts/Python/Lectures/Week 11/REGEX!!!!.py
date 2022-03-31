# using regex to censore social security numbers
import re #imports regex

def SSNregex(text):
    SSN = r"[0-9]{3}-[0-9]{2}-[0-9]{4}"
    SSN = r"\d{3}-\d{2}-\d{4}"                      # both are REGEX expressions for social security numbers
    output = re.sub(SSN, "-REDACTED-", text)        # REGEX command that substitutes SSN for Redacted
    return output

text = open("socialtest.txt", "r")
text = text.read() #opens and reads file

output = SSNregex(text)

product = open("socialtestfinal.txt", "w")
product.write(output)
product.close()


# way faster than using while loops and if statements

def longWayAround(text):
    SSN = False
    i = 0
    output = ""
    while i < (len(text)):
        if text[i] in "1234567890" and text[i+1] in "1234567890" and text[i+2] in "1234567890":
            if text[i+3] == "-":
                if text[i+4] in "1234567890"and text[i+5] in "1234567890":
                    if text[i+6] == "-":
                        if text[i+7] in "1234567890" and text[i+8] in "1234567890" and text[i+9] in "1234567890" and text[i+10] in "1234567890":
                            SSN = True
        if SSN == True:
            output += "-REDACTED-"
            i += 11
        else:
            output += text[i]
            i += 1
        
        SSN = False

    return output
text = "My social is 123-12-1234 LMAO!"
output = longWayAround(text)
print(output)


product = open("socialtestfinal.txt", "w")
product.write(output)
product.close()
