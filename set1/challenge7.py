import base64
import helper

key = "YELLOW SUBMARINE"

with open("7.txt", "rb") as f:
    ciphertext = base64.b64decode(f.read())

print helper.decryptAES(ciphertext, key)
