import helper

plaintext = "YELLOW SUBMARINE"*16


for i in range(0,20):
    ciphertext = helper.encryption_oracle(plaintext)
    print ciphertext.encode('hex')
