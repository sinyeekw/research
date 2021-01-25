def split(x):
    return x.split()

def extractletters(l):
    newList = []
    pos = 0
    for i in l:
        if(pos == 0 or (pos > 3 and pos < 9) or (pos > 13 and pos < 16) or pos == 18):
            newList.append(i[0])
        else:
            newList.append(i[0:2])
        pos += 1
    return newList

def mapPosition(splitedX, extractedWords):
    currPos = 0
    mapPos = {}
    wordCtr = 0
    for i in splitedX:
        mapPos[extractedWords[wordCtr]] = currPos
        # print(mapPos)
        currPos += len(i) + 1
        wordCtr += 1
    return mapPos

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
print(mapPosition(split(sentence), extractletters(split(sentence))))


