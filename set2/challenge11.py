import helper

plaintext = "YELLOW SUBMARINE"*16

nECB = 0
nCBC = 0

for i in range(0,10000):
    ciphertext = helper.encryption_oracle(plaintext)
    if helper.checkForECBEncryption(ciphertext,16):
        nECB += 1
    else:
        nCBC += 1

pECB = 100*float(nECB)/(nECB+nCBC)
print "ECB was used %f%%, CBC was used %f%%" % (pECB, 100.0 - pECB)
