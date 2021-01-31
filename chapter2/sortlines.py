with open("popularnames.txt") as reader, open("sorted.txt", "w") as sort:
    lines = [i.split('\t') for i in reader.readlines()]
    newLines = sorted(lines, key=lambda line: -int(line[2]))
    for line in newLines:
        strline = line[0] + " " + line[1] + " " + line[2] + " " + line[3]
        sort.write(strline)

