import re, json

with open("./enwiki-country.json") as reader, open("./media.txt", "w") as writer:
    article = reader.readlines()
    data = []
    for line in article:
        data = json.loads(line)
        if data['title'] == 'United Kingdom':
            break

    # . means any character, if DOTALL set, . means newline too, ? means only match 0/1 repetition of previously found RE
    # $ means match the end of a string/before a newline , () to match whatever inside 
    # .*? means match as much text as possible , ^ means match start of a string/newline character
    pattern = r'^\{\{Infobox country.*?$(.*?)^\}\}'
    info = re.findall(pattern, data['text'], re.MULTILINE + re.DOTALL)[0]
    # print(info)

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    fields = re.findall(pattern, info, re.MULTILINE + re.DOTALL) 
    #print(fields)

    fields = [(f[0].strip(), f[1].strip()) for f in fields]
    d1 = dict(field for field in fields)
    # print(d1)

d2 = {}
for entry in d1:
    # {m,n} means match from 2 to 5 repetitions of ', as much as possible 
    pattern = r'\'{2,5}'
    d2[entry] = re.sub(pattern, '',d1[entry])
    # print(d2[entry])

d3 ={}
for entry in d2:
    #?: means captured substr cannot be referenced/match by subsequent patterns, ?? means greedily match 
    pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    #\1 means reference first captured group 
    d3[entry] = re.sub(pattern, r'\1', d2[entry])
    print(d3[entry])
