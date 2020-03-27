import json
import click

DICTIONARY = "data/baseCharDict.json"
PUNC = ["，", "。", "；", "！", "？"]
PATTERN = {"平":"-", "上":"|", "去":"|", "入":"|"}

def readJson(js):
    with open(js, encoding="utf-8") as fd:
        cont = json.load(fd)
        return cont

@click.command()
@click.argument('words')
def search(words):
    data = readJson(DICTIONARY)
    result = ''
    pattern = ''

    if True:
        from opencc import OpenCC
        cc = OpenCC('t2s')
        words = cc.convert(words)

    for word in words:
        if word in PUNC:
            result += '\n'
            pattern += word
            continue

        result += word + ' : '
        thisPattern = ''
        try:
            # "观": [["平", "十四寒", "观看"], ["上",  "十五翰",  "楼观"]]
            
            for items in data[word]:
                if True:
                    if thisPattern == '':
                        thisPattern = PATTERN[items[0]]
                    elif thisPattern != PATTERN[items[0]]:
                        thisPattern = '?'
                
                if len(items[2]) == 0:
                    result += items[0] + " " + items[1]
                else:
                    result += items[0] + " " + items[1] + "(" + items[2] + ")"
                result += "; "
            
            pattern += thisPattern
        except:
            pass
        result += '\n'
    click.echo(result)
    click.echo(pattern)


if __name__ == '__main__':
    search()