from nltk import ngrams


def split(x):
    return list(x)

def bi_gram(x):
    return ngrams(x,2)

def createSet(grams):
    l = set()
    for gram in grams:
        #print(gram)
        l.add(gram)
    return l

def printGram(grams):
    for gram in grams:
        print(gram)
sentence1 = split("paraparaparadise")
sentence2 = split("paragraph")

biGram1 = createSet(bi_gram(sentence1))
biGram2 = createSet(bi_gram(sentence2))

print("Intersection")
print(biGram1.intersection(biGram2))

print("Union")
print(biGram1.union(biGram2))

print("Difference")
print(biGram1.difference(biGram2))

print("Check if 'se' is in both sets")
print((('s','e') in biGram1) and (('s','e') in biGram2))

# suggested ans
# X = set(ngrams("paraparaparadise", 2))
# Y = set(ngrams("paragraph", 2))

# union = X | Y
# intersection = X & Y
# difference = X - Y

# bigram = ('s', 'e')
# print(bigram in X, bigram in Y)