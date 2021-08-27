# Write your code here
import random


def fileopen():
    filename = input()
    try:

        file = open(filename, "r", encoding="utf-8")
        tokenlist = file.read().split()
        file.close()
        return tokenlist
    except FileExistsError:

        print("Failed to read the file.")


def tokens(tokenlist):
    print("Corpus statistics")
    print("All tokens: %d" % len(tokenlist))
    print("Unique tokens: %d" % len(set(tokenlist)))

    while True:
        userinput = input()
        if userinput == "exit":
            break
        try:
            userinput = int(userinput)
        except:
            print("Type Error")
            continue
        try:
            print(tokenlist[userinput])
        except IndexError:
            print("Index Error")


def bigramlist(tokenlist):
    bigramlist = []
    for x in range(len(tokenlist) - 1):
        bigramlist.append("%s %s" % (tokenlist[x], tokenlist[x + 1]))
    return bigramlist


def trigramlist(tokenlist):
    trigramlist = []
    for x in range(len(tokenlist) - 2):
        trigramlist.append("%s %s %s" % (tokenlist[x], tokenlist[x + 1], tokenlist[x + 2]))
    return trigramlist


def tritails(trigramlist):
    tailsdict = {}
    for x in trigramlist:
        head = x.split(" ")[0] + " " + x.split(" ")[1]
        tailsdict[head] = {}

    for x in trigramlist:
        head = x.split(" ")[0] + " " + x.split(" ")[1]
        tail = x.split(" ")[2]
        if tail in tailsdict[head]:
            x = tailsdict[head][tail]
            tailsdict[head][tail] = x + 1
        else:
            tailsdict[head][tail] = 1
    return tailsdict


def tails(bigramlist):
    tailsdict = {}
    for x in bigramlist:
        head = x.split(" ")[0]
        tailsdict[head] = {}

    for x in bigramlist:
        head = x.split(" ")[0]
        tail = x.split(" ")[1]
        if tail in tailsdict[head]:
            x = tailsdict[head][tail]
            tailsdict[head][tail] = x + 1
        else:
            tailsdict[head][tail] = 1
    return tailsdict


def output(tails):
    while True:
        userinput = input()
        if userinput == "exit":
            break
        try:
            print("Head: %s" % userinput)
            for x in tails[userinput]:
                print("Tail: %s Count: %d" % (x, tails[userinput].get(x)))

        except:
            print("The requested word is not in the model. Please input another word.")
            continue


def firstword(tails):
    b = ""
    c = "?"
    while not (b.isupper() and c not in ['.', '!', '?']):
        a = random.choice(list(tails.keys()))
        b = a[0]
        c = a[-1:]
    return a


def lastword(tails):
    b = ""
    while b not in ['.', '!', '?']:
        a = random.choice(list(tails.keys()))
        b = a[-1:]
    return a


def randomtext(tails):
    for y in range(10):
        sentence = firstword(tails)
        last = sentence
        for j in range(4):
            if j == 3:
                x = lastword(tails)
            else:
                if sentence[-1:] in ['.', '!', '?']:
                    x = firstword(tails)
                else:
                    x = random.choices(list(tails[last]), tails[last].values())[0]
            sentence += " %s" % x
            last = sentence.split()[-2] + " " + sentence.split()[-1]

        print(sentence)


randomtext(tritails(trigramlist(fileopen())))
