def splitfile(filename, n):
    numLines = countLines(filename)
    with open(filename+".txt") as reader, open("output.txt", "w") as output:
        for i in range(n -1):
            for i in range(numLines//n):
                output.write(reader.readline())
            output.write("\n")
        for i in range(numLines%n + numLines//n):
            output.write(reader.readline())




def countLines(filename):
    numLines = 0
    with  open(filename+".txt") as reader:
        for i in reader:
            numLines += 1
    return numLines


splitfile("merge", 3)