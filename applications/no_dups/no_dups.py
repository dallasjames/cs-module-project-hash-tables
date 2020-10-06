def no_dups(s):
    s = s.split(" ")
    news = ""
    if len(s) == 0:
        return ""
    for i in s:
        if i not in news:
            news += " " + i
    news = news.strip()
    return news


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
