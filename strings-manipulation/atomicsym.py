def split(x):
    return x.split()

def extractletters(l):
    newList = []
    pos = 0
    # newList = [w[0] if i in [0,4,5,6,7,8,14,15,18] else w[:2] for i, w in enumerate(l)]
    for i in l:
        if(pos in [0,4,5,6,7,8,14,15,18]):
        #if(pos == 0 or (pos > 3 and pos < 9) or (pos > 13 and pos < 16) or pos == 18):
            newList.append(i[0])
        else:
            newList.append(i[0:2])
        pos += 1
    return newList

def mapPosition(x,elements, splitedX):
    # currPos = 0
    # mapPos = {}
    # wordCtr = 0
    # for i in splitedX:
    #     mapPos[extractedWords[wordCtr]] = currPos
    #     # print(mapPos)
    #     currPos += len(i) + 1
    #     wordCtr += 1
    mapPos = {}
    for (e, w) in zip(elements, splitedX):
        offset = x.find(w)
        mapPos[e] = offset
    return mapPos

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
print(mapPosition(sentence,extractletters(split(sentence)), split(sentence)))


