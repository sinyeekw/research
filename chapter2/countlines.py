reader = open("popularnames.txt","r")
numLines = 0
for i in reader:
    numLines += 1

print(numLines)