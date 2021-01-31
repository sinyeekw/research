def firstn(filename, n):
    firstNLines = []
    with open(filename+".txt") as reader:
        for i in range(n):
            line = reader.readline()
            firstNLines.append(line[:-2])
    
    return firstNLines

print(firstn("merge", 5))

