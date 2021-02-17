import json
with open('./enwiki-country.json') as f, open('./uk.txt', "w") as writer:
    lines = f.readlines()
    for line in lines:
        data = json.loads(line)
        if data['title'] == 'United Kingdom':
            writer.writelines(json.dumps(data))
            break
