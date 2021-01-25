def splitstr(x):
    return x.split()

def countAlpha(arr):
    l = []
    for i in arr:
        l.append(len(i))
    return l


print(countAlpha(splitstr("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics")))