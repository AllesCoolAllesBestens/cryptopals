from Crypto.Util.strxor import strxor
import helper
import base64
s1 = "this is a test"
s2 = "wokka wokka!!!"
text = ""
with open("6.txt", "r") as f:
    text = base64.b64decode(f.read())

if text == "":
    print "error reading file"
    exit()

test = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

keysize = helper.findKeysize(test.decode('hex'))


#keysize = helper.findKeysize(text.encode('hex'))
print keysize
