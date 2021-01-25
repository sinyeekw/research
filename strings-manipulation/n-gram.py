from nltk import ngrams

def split(x):
    return x.split()

def bi_gram(x):
    return ngrams(x,2)

def printGram(grams):
    for gram in grams:
        print(gram)

sentence = "I am an NLPer"
splited = sentence.split()
x = bi_gram(splited)
printGram(x)

print(splited)
for i in splited:
    z = bi_gram(i)
    printGram(z)

