with open("ciphertext.txt") as f:
    letters = f.read()
ldict = {}
for i in letters:
    if i in ldict:
        ldict[i] += 1
    else:
        ldict[i] = 1
sums = 0
for i in ldict:
    if i.isalnum():
        sums += ldict[i]
for i in ldict:
    ldict[i] *= 100
    ldict[i] /= sums
    ldict[i] = round(ldict[i], 2)
print(ldict)
cipherDict = {
    "E": 11.53,
    "T": 9.75,
    "A": 8.46,
    "O": 8.08,
    "H": 7.71,
    "N": 6.73,
    "R": 6.29,
    "I": 5.84,
    "S": 5.56,
    "D": 4.74,
    "L": 3.92,
    "W": 3.08,
    "U": 2.59,
    "G": 2.48,
    "F": 2.42,
    "B": 2.19,
    "M": 2.18,
    "Y": 2.02,
    "C": 1.58,
    "P": 1.08,
    "K": 0.84,
    "V": 0.59,
    "Q": 0.17,
    "J": 0.07,
    "X": 0.07,
    "Z": 0.03
}
decodedDict = {}
for i in ldict:
    if i.isalnum():
        for d in cipherDict:
            if ldict[i] == cipherDict[d]:
                decodedDict[i] = d

output = ""
transtable = output.maketrans(decodedDict)
output = letters.translate(transtable)
print(output)
