def concat(x1, x2):
    #return ''.join(''.join(f for f in tup) for tup in zip(x1,x2))
    return "".join([c1 + c2 for (c1, c2) in zip(x1, x2)])

def concat2(x1,x2):
    return ''.join(map(''.join, zip(x1, x2)))

print(concat("abcdef", "ghijkl"))
print(concat2("123456", "789012"))
    