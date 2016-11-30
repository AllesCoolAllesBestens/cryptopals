from Crypto.Cipher import AES
import base64

key = "YELLOW SUBMARINE"

with open("7.txt", "rb") as f:
    ciphertext = base64.b64decode(f.read())

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print plaintext
