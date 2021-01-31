from collections import Counter

with open("popularnames.txt") as reader, open("sortbystr.txt", "w") as sort:
    lines = reader.readlines()
    names = [line.split('\t')[0] for line in lines]
    counter = Counter(names)
    def key_func(line):
        row = line.split('\t')
        name = row[0]
        return -counter[name]
    
    newLines = sorted(lines, key=key_func)
    print(newLines)
    
    for line in newLines:
        sort.write(line)

