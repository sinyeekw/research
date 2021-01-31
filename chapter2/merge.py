with open("replacedfile.txt") as reader, open("merge.txt","w") as merge:
    for i in reader:
        splited = i.split(" ")
        merge.write(splited[0] +" " + splited[1] + "\n")
        