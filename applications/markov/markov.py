import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
test = "Banana 1 three banana 1 1 banana 2 2 three banana. \"Start stop.\""
words = words.strip("\n")
words = words.split(" ")

word_dict = {}

for index, word in enumerate(words):
    if word in word_dict:
        if index + 1 < len(words):
            word_dict[word].append(words[index + 1])
        else:
            word_dict[word] = None
    else:
        if index + 1 < len(words):
            word_dict[word] = [words[index + 1]]
        else:
            word_dict[word] = None


# TODO: construct 5 random sentences
def markov_sentence(word_dict):
    punctuation = ".?!"
    starters = []
    stoppers = []
    for word in word_dict:
        if word[0].isupper() or (word[0] == "\"" and word[1].isupper()):
            starters.append(word)
        if word[-1] in punctuation or (word[-1] == "\"" and word[-2] in punctuation):
            stoppers.append(word)
    string = ""
    word = random.choice(starters)
    while word not in stoppers:
        string += word + " "
        word = random.choice(word_dict[word])
    string += word + " "
    return string


print(markov_sentence(word_dict))
