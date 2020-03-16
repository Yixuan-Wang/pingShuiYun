import json
import sys

if len(sys.argv) <= 1:
    print("usage: %s jsonFile 看 元" % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], encoding="utf-8") as fd:
    cont = json.load(fd)

    for ch in sys.argv[2:]:
        # each char
        print(ch)
        for item in cont[ch]:
            print("   %s %s" % (item[0], item[1]))

