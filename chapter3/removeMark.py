import re, json

with open("./enwiki-country.json") as reader, open("./media.txt", "w") as writer:
    article = reader.readlines()
    data = []
    for line in article:
        data = json.loads(line)
        if data['title'] == 'United Kingdom':
            break

    pattern = r''