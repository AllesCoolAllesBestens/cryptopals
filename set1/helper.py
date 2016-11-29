from collections import Counter
import math
from scipy import spatial
import string

def xor_string(s1, s2):
    assert len(s1) == len(s2)
    output = ""
    for c1,c2 in zip(s1.decode('hex'), s2.decode('hex')):
        output += chr(ord(c1) ^ ord(c2))

    return output.encode('hex')

def xor_char(s1, c1):
    output = ""
    for c in s1.decode('hex'):
        output += chr(ord(c1) ^ ord(c))

    return output.encode('hex')

def encryptRepeatingKey(text, key):
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
    allLetters = set(letterFrequency.keys())

    letters = dict.fromkeys(allLetters, 0)
    letters.update(Counter(text.lower()))
    usedLetters = set(letters.keys())
    to_compare = sorted(usedLetters & allLetters)

    vAvgFreq = [letterFrequency[x]*100 for x in to_compare]
    vUsedFreq = [letters[x] for x in to_compare]
    assert len(vUsedFreq) == len(vAvgFreq)
    if len(vUsedFreq) == 0:
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
        #printable = all(c in string.printable for c in _output.decode('hex'))
        printable = True
        if _score > score and printable:

            score = _score
            output = _output
            char = chr(i)

    return (score, output, char)



