import json
import yaml
import sys

if len(sys.argv) <= 1:
    print("usage: %s jsonFile" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], encoding='utf-8') as baseCharJson:
    cont = json.load(baseCharJson)
    print(yaml.dump(cont, allow_unicode=True, sort_keys=False))