import helper
import base64

s1 = "this is a test"
s2 = "wokka wokka!!!"
assert helper.hammingDistance(s1,s2) == 37

with open("6.txt","rb") as f:
    cipher = base64.b64decode(f.read())

keysize = helper.findKeysize(cipher, nBlocks=4)

blocks = helper.transponseCipher(cipher, keysize[0])
key = ""
for block in blocks:
    key += helper.findSingleByteXorChar(block.encode('hex'))[2]


print helper.xorWithRepeatingKey(cipher, key)
print "\n\nEncrypted with Key: '%s'" % (key)
