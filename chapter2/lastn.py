def lastn(filename, n):
    reader = open(filename+".txt")
    lines = reader.readlines()
    toReturn = []
    for i in lines:
        toReturn.append(i[:-1])
    return toReturn[-n:]


print(lastn("merge",5))
