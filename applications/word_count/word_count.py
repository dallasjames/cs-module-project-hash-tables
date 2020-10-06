import string


def word_count(s):
    s = s.replace("\r", " ")
    s = s.replace("\n", " ")
    s = s.replace("\t", " ")
    words_with_punc = s.lower().split(" ")
    count = {}
    if len(s) > 0:
        for i in words_with_punc:
            words = i.strip(string.punctuation)
            if len(words) > 0:
                if words in count:
                    count[words] += 1
                else:
                    count[words] = 1
    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))