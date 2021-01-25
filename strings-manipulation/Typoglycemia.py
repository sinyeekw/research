import random

def typoglycemia(x):
    splitX = x.split()

    ctr = 0
    for i in splitX:
        if(len(i) > 4):
            s = i[0] + shuffleLetters(i[1:-1]) + i[-1]
            splitX[ctr] = s
        ctr += 1
    return " ".join(splitX)

def shuffleLetters(word):
    chars = list(word)
    random.shuffle(chars)
    return "".join(chars)

print(typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"))
