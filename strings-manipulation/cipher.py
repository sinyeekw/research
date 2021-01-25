def cipher(x):
    splitX = list(x)
    ctr = 0
    for i in splitX:
        if(i == 'c'):
            splitX[ctr] = chr(219 - ord('c'))
        ctr += 1
    return ''.join(splitX)

def dicipher(x):
    splitX = list(x)
    ctr = 0
    for i in splitX:
        if(i == 'x'):
            splitX[ctr] = chr(219 - ord('x'))
        ctr += 1
    return ''.join(splitX)

print(cipher("I am a potato ball cme Crumble in colourful crayons."))
modi = cipher("I am a potato ball cme Crumble in colourful crayons.")
print(dicipher(modi))