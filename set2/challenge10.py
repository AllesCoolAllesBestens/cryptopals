import helper
import base64

test_plaintext = "AAAABBBBCCCCDDDD"*50
test_key = "test"*4
test_cipher = helper.encryptAES(test_plaintext, test_key)
#assert helper.decryptAES(test_cipher, test_key) == test_plaintext

IV = "\x00"*16
ciphertext = helper.encryptAES_CBC(test_plaintext, test_key, IV)
ciphertextEBC = helper.encryptAES(test_plaintext, test_key)
plaintext = helper.decryptAES_CBC(ciphertext, test_key, IV)
with open("10.txt", "rb") as f:
    ciphertext = base64.b64decode(f.read())


plaintext = helper.decryptAES_CBC(ciphertext, "YELLOW SUBMARINE", IV)
print plaintext


