def unique(filename):
    reader = open(filename +".txt")
    lines = reader.readlines()
    names = []
    for i in lines:
        i = i.split()[0]
        if i not in names:
            names.append(i)
    return names

print(unique("merge"))
        