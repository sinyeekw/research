import re

with open('./categories.txt') as reader, open('./categoriesNames.txt', "w") as writer:
    pattern = r'\[\[Category:(.+?)\]\]'
    for line in reader.readlines():
        line = re.search(pattern, line)
        writer.writelines(str(line.group(1)) + "\n")
