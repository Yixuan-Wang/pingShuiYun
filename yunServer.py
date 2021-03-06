import json
import sys

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/char', methods=['GET'])
def char():
    words = request.args.get('q', '')
    print(words)
    return search(words)

def search(words):
    result = ''
    for word in words:
        result += word + ' : '
        try:
            # "观": [["平", "十四寒", "观看"], ["上",  "15翰",  "楼观"]]
            for items in data[word]:
                if len(items[2]) == 0:
                    result += items[0] + " " + items[1]
                else:
                    result += items[0] + " " + items[1] + "(" + items[2] + ")"
                result += "; "
        except:
            pass
        result += '<br>\n'
    return result

def readJson(js):
    with open(js, encoding="utf-8") as fd:
        cont = json.load(fd)
        return cont

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("usage: %s jsonFile" % sys.argv[0])
        sys.exit(1)
    data = readJson(sys.argv[1])

    app.run()

