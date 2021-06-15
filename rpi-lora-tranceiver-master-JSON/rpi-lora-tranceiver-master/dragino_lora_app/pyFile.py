import json import os import re

with open ("program.txt", "rt") as myfile: for myline in myfile: release = re.sub(r"(?<=\d)\s+", "\n", myline) #print(release) #myfile.close()

with open("program2.txt", "w") as f: f.write(release) f.close()

filename = "program2.txt" dict1 = {} with open(filename) as fh: for line in fh: command, description = line.strip().split(None,1) dict1[command] = description.strip()

with open('testData.json','w') as json_file: json.dump(dict1, json_file)