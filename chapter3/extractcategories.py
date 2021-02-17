import json
import re
with open('./uk.txt') as reader, open('./categories.txt', "w") as writer:
    for line in reader.readlines():
        t = re.findall(r"\[\[Category:.+\]\]", line)
        if len(t) != 0: 
            writer.writelines(str(t) +"\n")
       
        
