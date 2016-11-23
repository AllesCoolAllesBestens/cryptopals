import collections
from Crypto.Util.strxor import strxor_c, strxor


def findKeysize(text, maxSize=40):
    keysize = (1000, -1)
#    print text
    for i in range(2, maxSize):
        if 2*i > len(text):
            break
        s1 = text[:i]
        s2 = text[i:2*i]
        print (s1, s2)
        print "ok"

        n_dist = float(hamming_distance(s1,s2))/float(i)
        print (s1, s2, n_dist)
        if n_dist < keysize[0]:
            keysize = (n_dist, i)

    return keysize

def hamming_distance(s1, s2):
    if(len(s1) != len(s2)):
        print "Hamming distance: Stringlength doesn't match!"
        exit()

    slen = len(s1)
    diff = xor_hexstream(s1,s2)

    distance = 0
    for c in diff:
        distance += bin(ord(c)).count("1")
    return distance

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    result = []
    for start in range(0, len(s), n):
        result.append(s[start:start+n])
    return result

def getMostProbableEnglishString(text):
    englishLetterFreq = {' ': 1, 'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

    bestString = ""
    bestStringMetric = -1000
    key = ""

    for char in range(0,128):    # a-z
        dec = strxor_c(text.decode('hex'), char)
        declen = len(dec)
        letters = collections.Counter(dec)
        sum = 0
        for letter in letters:
            if letter.upper() in englishLetterFreq:
                sum += (float(letters[letter])/float(declen)) * englishLetterFreq[letter.upper()]
            else:
                sum -= 0.4

        if sum > bestStringMetric:
            bestStringMetric = sum
            bestString = dec
            key = chr(char)

    return bestString, bestStringMetric, key

