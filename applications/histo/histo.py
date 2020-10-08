import string


with open("robin.txt") as f:
    page = f.read()


def histo(words):
    hgram = {}
    words = words.translate(str.maketrans('', '', string.punctuation))
    words = words.lower()
    words = words.replace("\r", " ")
    words = words.replace("\n", " ")
    words = words.replace("\t", " ")
    words = words.split(" ")
    for i in words:
        if i in hgram:
            hgram[i] += "#"
        else:
            hgram[i] = "#"

    dictionary_items = hgram.items()
    sorted_items = sorted(dictionary_items)
    for key, value in sorted_items:
        print(key, ' : ', value)


histo(page)
