from collections import Counter
import math
from scipy import spatial
import string
import itertools
from Crypto.Cipher import AES
import random

"""
http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
"""
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def getRandomKey(size=16):
    key = ""
    for i in range(size):
        key += chr(random.randint(0, 127))
    return "".join(key)

def encryption_oracle(plaintext):
    key = getRandomKey()
    plaintext = "A"*random.randint(5,10)+plaintext+"A"*random.randint(5,10)

    if random.random() > 0.5:
        return encryptAES(plaintext, key)
    else:
        IV = getRandomKey(16)
        return encryptAES_CBC(plaintext,key,IV)





def xor_string(s1, s2):
    assert len(s1) == len(s2)
    output = ""
    for c1,c2 in zip(s1.decode('hex'), s2.decode('hex')):
        output += chr(ord(c1) ^ ord(c2))

    return output.encode('hex')

def checkForECBEncryption(ciphertext, blocksize):
    blocks = []
    for i in range(len(ciphertext)/blocksize):
        block = ciphertext[i*blocksize:blocksize*(i+1)]
        if block in blocks:
            return True
        blocks.append(block)

    return False

def decryptAES(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

def encryptAES(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = padPKCS7(plaintext, 16)
    return cipher.encrypt(plaintext)

def encryptAES_CBC(plaintext, key, IV):
    plaintext = padPKCS7(plaintext, 16)
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = [None] * len(blocks)
    for i in range(len(blocks)):
        plain_in = blocks[i]
        if i == 0:
            plain_in = xor_string(IV.encode('hex'), plain_in.encode('hex'))
        else:
            plain_in = xor_string(ciphertext[i-1].encode('hex'),
                                plain_in.encode('hex'))

        ciphertext[i] = encryptAES(plain_in.decode('hex'),key)
    return "".join(ciphertext)

def decryptAES_CBC(ciphertext, key, IV):
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plaintext = [None] * len(blocks)

    for i in range(len(blocks)):
        decrypted = decryptAES(blocks[i],key)
        if i == 0:
            decrypted = xor_string(IV.encode('hex'), decrypted.encode('hex'))
        else:
            decrypted = xor_string(blocks[i-1].encode('hex'), decrypted.encode('hex'))

        plaintext[i] = decrypted.decode('hex')

    return "".join(plaintext)


"""

As described in https://tools.ietf.org/html/rfc2315 Section 10.3
"""
def padPKCS7(key, blocksize):
    l = len(key)
    k = blocksize
    if l % k == 0:
        return key
    padsize = k - (l % k)
    return key.ljust(len(key)+padsize, chr(padsize))


def xor_char(s1, c1):
    output = ""
    for c in s1.decode('hex'):
        output += chr(ord(c1) ^ ord(c))

    return output.encode('hex')

def transponseCipher(cipher, keysize):
    blocks = [''] * keysize
    for i in range(len(cipher)):
        blocks[i%keysize] += cipher[i]

    return blocks


def hammingDistance(s1, s2):
    xored = xor_string(s1.encode('hex'),s2.encode('hex'))
    return sum([bin(ord(x)).count("1") for x in xored.decode('hex')])

def avgHammingDistance(*words):
    assert len(words) > 1                   # at least 2 words
    assert len(words) % 2 == 0              # word count shoult be a
                                            # multiple of 2
    n = len(words[0])
    assert n > 0                            # length of word > 0
    assert all(len(x) == n for x in words)  # all words are of the same length
    sumDistance = 0


    distances = map(lambda (x,y): hammingDistance(x,y),
            list(itertools.combinations(words,2)))
    return float(sum(distances))/float(len(distances))

def findKeysize(cipher, nBlocks=2, maxKeysize=40):
    keysize = []
    for i in range(2, maxKeysize+1):
        words = []
        for n in range(nBlocks):
            words.append(cipher[n*i:(n*i)+i])
        keysize.append((i,avgHammingDistance(*words)/i))

    return sorted(keysize, key=lambda tup: tup[1])[0]



def xorWithRepeatingKey(text, key):
    output = ""
    for i in range(len(text)):
        output += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return output



"""
letterFrequency = {
        'a':8.167, 'b':1.492, 'c':2.782, 'd':4.253,
        'e':12.702, 'f':2.228, 'g':2.015, 'h':6.094,
        'i':6.966, 'j':0.153, 'k':0.772, 'l':4.025,
        'm':2.406, 'n':6.749, 'o':7.507, 'p':1.926,
        'q':0.095, 'r':5.987, 's':6.327, 't':9.056,
        'v':0.987, 'w':2.360, 'x':0.150, 'y':1.974,
        'z':0.074 }
"""
letterFrequency = {
    " ": 18.28846265,
    "e": 10.26665037,
    "t": 7.51699827,
    "a": 6.53216702,
    "o": 6.15957725,
    "n": 5.71201113,
    "i": 5.66844326,
    "s": 5.31700534,
    "r": 4.98790855,
    "h": 4.97856396,
    "l": 3.31754796,
    "d": 3.28292310,
    "u": 2.27579536,
    "c": 2.23367596,
    "m": 2.02656783,
    "f": 1.98306716,
    "w": 1.70389377,
    "g": 1.62490441,
    "p": 1.50432428,
    "y": 1.42766662,
    "b": 1.25888074,
    "v": 0.79611644,
    "k": 0.56096272,
    "x": 0.14092016,
    "j": 0.09752181,
    "q": 0.08367550,
    "z": 0.05128469,
}

def englishTextScore(text):
    text = text.lower()
    textlen = len(text)
    allLetters = set(letterFrequency.keys())

    letters = dict.fromkeys(allLetters, 0)
    letters.update(Counter(text.lower()))
    usedLetters = set(letters.keys())
    to_compare = sorted(usedLetters & allLetters)

    vAvgFreq = [(float(letterFrequency[x])/float(textlen))*100
                    for x in to_compare]
    vUsedFreq = [letters[x] for x in to_compare]
    assert len(vUsedFreq) == len(vAvgFreq)
    assert len(vUsedFreq) > 0 and len(vAvgFreq) > 0
    if sum(vUsedFreq) == 0:
        return 0

    cos_distance = (1 - spatial.distance.cosine(vAvgFreq, vUsedFreq))
    lengthFactor = len(to_compare)
    return cos_distance


    """

    # This is old code implementing the cosine distance.
    # Left this for comprehension
    dot = 0
    magA = 0
    magB = 0
    for a,b in zip(vAvgFreq, vUsedFreq):
        dot += a*b
        magA += a*a
        magB += b*b


    if magA == 0 or magB == 0:
        return 0

    similarity = dot/(math.sqrt(magA)*math.sqrt(magB))

    """

def findSingleByteXorChar(text):
    score = -1
    output = ""
    char = ""
    for i in range(1,255 + 1):
        _output = xor_char(text, chr(i))
        _score = englishTextScore(_output.decode('hex'))
        """
        Might be working without the check for printables now
        """
        #printable = all(c in string.printable for c in _output.decode('hex'))
        printable = True
        if _score > score and printable:

            score = _score
            output = _output
            char = chr(i)

    return (score, output, char)



