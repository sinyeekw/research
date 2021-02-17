import re
import json
with open('./enwiki-country.json') as reader, open('./sections.txt', "w") as writer:
    pattern = "==.+=="
    article = reader.readlines()
    data = []
    for line in article:
        data = json.loads(line)
        if data['title'] == 'United Kingdom':
            break


    sections = re.findall("==.+==", data['text'])
    section_names = []
    for section in sections:
        section_level = int(len(re.findall('=', section)) / 2 - 1)
        section_name = section.replace('=', '') 
        writer.writelines(str(section_level) +" " + str(section_name) +"\n")