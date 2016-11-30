import helper

with open("8.txt", "rb") as f:
    for line in f:
        ciphertext = line.strip()
        if helper.checkForECBEncryption(ciphertext.decode('hex'), 16):
            print "Found possible ECB Encrypted ciphertext: "
            print ciphertext



