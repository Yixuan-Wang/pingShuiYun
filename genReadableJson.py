import json
import sys

if len(sys.argv) <= 1:
    print("usage: %s jsonFile" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], encoding='utf-8') as baseCharJson:
    cont = json.load(baseCharJson)
    print(json.dumps(cont, ensure_ascii=False, indent=4))