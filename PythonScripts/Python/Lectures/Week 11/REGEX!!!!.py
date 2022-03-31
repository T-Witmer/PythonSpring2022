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
