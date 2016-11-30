import helper

key = "YELLOW SUBMARINE"
paddedKey = helper.padPKCS7(key, 20)
print list(paddedKey)
