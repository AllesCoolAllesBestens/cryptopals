import helper

result = (0,"","")
with open("4.txt", "rb") as f:
    for line in f:
        output = helper.findSingleByteXorChar(line.strip())
        if output[0] > result[0]:
            result = output

print result[1].decode('hex')

