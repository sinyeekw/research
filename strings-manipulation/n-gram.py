from nltk import ngrams

def split(x):
    return x.split()

def bi_gram(x):
    return ngrams(x,2)

def printGram(grams):
    for gram in grams:
        print(gram)

# def ngrams(seq, n):
#     if isinstance(seq, str):
#         seq = [s for s in seq]
    
#     seq.insert(0, "__head__")
#     ret = []
#     for i, s in enumerate(seq):
#         condition = i < len(seq) - 1
#         tup = (seq[i], seq[i+1]) if condition else (seq[i], "__end__")
#         ret.append(tup)
    
#     return ret

sentence = "I am an NLPer"
splited = sentence.split()
x = bi_gram(splited)
printGram(x)

print(splited)
for i in splited:
    z = bi_gram(i)
    printGram(z)

