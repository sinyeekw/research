reader = open("popularnames.txt","r")
output = open("replacedfile.txt", "w")

for i in reader:
    newLine = i.replace('\t', ' ')
    output.write(newLine)

