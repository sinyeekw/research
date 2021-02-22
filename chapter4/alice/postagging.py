import spacy
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
nlp = spacy.load('en_core_web_sm')


with open('./alice.txt') as reader:
    lines = []
    raw = reader.read().split('\n')
    for line in raw:
        if line == 'EOS' or line == ' ' or line == '':
            continue
        lines.extend(line.split('. '))

text = []
j = 0
for i in lines:
    a = nlp(i)
    for token in a: 
        # print(token.text, token.pos_, token.tag_)
        b = [token.text, token.pos_, token.lemma_]
        text.append(b)

# print(text)

# extracting verbs & lemmas of verbs

# verbs = []
# lemmas = []
# for i in text: 
#     if i[1] == "VERB":
#         verbs.append(i)
#         lemmas.append(i[2])


# print(verbs)
# print(lemmas)

#extracting nouns in form A of B where A and B are nouns 

# sets = []
# length = len(text) - 2
# i = 0
# while i != length:
#     if text[i][1] == "NOUN" and text[i+1][2] == "of" and text[i+2][1] == "NOUN":
#         sets.append([text[i][0], text[i+1][2], text[i+2][0]])
#     i += 1

# print(sets)

# Extract frequency of words, sort by desc 

dict1 = {}
for i in text:
    lower = str(i[0]).lower()
    if not lower.isalpha():
        continue
    if lower not in dict1:
        dict1[lower] = 1 
    else:
        dict1[lower] = dict1.get(lower) + 1

# print(dict1)

# sort dict

# dict2 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
# # print(dict2)
# dict2items = dict2.items()
# # obtain top-10 most frequent words 
# i = 0
# xaxis = []
# yaxis = []
# for k, v in dict2items:
#     if(i == 10):
#         break
#     # print(k)
#     xaxis.append(k)
#     yaxis.append(v)
#     i += 1

# visualise top-10
# plt.bar(xaxis, yaxis)
# plt.title('top 10 most frequent words')
# plt.xlabel('words')
# plt.ylabel('frequency')
# plt.show()


#co-occuring words (collocation) -- can use enumerate, bi-gram, 

# words = []
# dict3 = {}
# pos = 0
# while pos != len(text) -1:
#     # t1 = str(text[pos][0]).lower()
#     # t2 = str

#     if(text[pos][0]== "Alice"):
#         if str(text[pos+1][0]).isalpha() and text[pos+1][0] not in dict3:
#             dict3[ text[pos+1][0]] = 1
#         elif str(text[pos+1][0]).isalpha():
#             dict3[ text[pos+1][0]] = dict3.get( text[pos+1][0]) + 1

    #     # words.append(text[pos+1][0])
    # elif ( text[pos+1][0] == "Alice"):
    #     if str(text[pos][0]).isalpha() and text[pos][0] not in dict3:
    #         dict3[text[pos][0]] = 1
    #     elif str(text[pos][0]).isalpha() :
    #         dict3[text[pos][0]] = dict3.get( text[pos][0]) + 1
    #     # words.append(text[pos][0])
    # pos += 1
    

# print(words)
# print(dict3)

# sort dict
# dict4 = dict(sorted(dict3.items(), key=lambda item: item[1], reverse=True))
# print(dict4)
# dict4items = dict4.items()
# # obtain top-10 most frequent words 
# i = 0
# xaxis1 = []
# yaxis1 = []
# for k, v in dict4items:
#     if(i == 10):
#         break
#     # print(k)
#     xaxis1.append(k)
#     yaxis1.append(v)
#     i += 1

# # visualise top-10
# plt.bar(xaxis1, yaxis1)
# plt.title('top 10 most frequent words with Alice')
# plt.xlabel('words')
# plt.ylabel('frequency')
# plt.show()

#Plot word frequency histogram
# xaxis2 = []
# yaxis2 = []

# for k,v in dict1.items():
#     xaxis2.append(k)
#     yaxis2.append(v)

# plt.bar(list(dict1.keys()), dict1.values(), color='g')
# plt.show()
    

#Zipf law
# x = 2000
# y = x*2
# lengthdict = len(dict1)
# indices = []
# for i in range(lengthdict):
#     indices.append(i)

# data = pd.DataFrame(dict1, index = indices )
# fig, ax = plt.subplots()
# ax.set(xscale="log", yscale="log")
# sb.regplot(x, y, data, ax=ax, scatter_kws={"s": 100})
# plt.show()





