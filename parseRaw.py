import os
import sys
import json


def checkRawFile(argv):
    if len(argv) != 2:
        print("usage: %s file" % argv[0])
        sys.exit(-1)
    name = argv[1]
    if not os.path.exists(name):
        print("source file: %s not exist!" % name)
        sys.exit(-2)
    return name


def readRawFile(inFile):
    ''' contents:
          十三元平=+言园源原...;  空行； 其它...;
          僻字行(可能有多行)...;
    '''
    with open(inFile, 'r', encoding='utf-8') as fd:
        originDic = {}
        for line in fd.readlines():
            line = line.strip()
            if line.startswith('其它') or len(line) == 0:
                continue

            # use "+" for split, "=" for header falg
            lineList = line.split('+', 1)
            if lineList[0].endswith('='):
                headers = lineList[0][:-1]
                originDic[headers] = lineList[1]
            else:
                originDic[headers] += lineList[0]
    return originDic


def genDict(oriDic):
    ''' eg: "十三元平": "言园源原喧轩翻繁元垣猿援[引也]萱 '''
    yunDic = {}
    yunCatDic = {}
    for (header, conts) in oriDic.items():
        yun, sheng = header[:-1], header[-1]
        yunCat = sheng + yun

        # print(cont.decode("utf-8"))
        print("-- origin: %s" % conts)
        cLen = len(conts)
        idx, start = 0, -1
        while idx < cLen:
            note = ''
            if idx+1 < cLen and conts[idx+1] == '[':
                start = idx+2   # read for read notes
                while conts[start] != ']':
                    note += conts[start]
                    start += 1
                print("%d: %s<%s> " % (idx, conts[idx], note))
            else:
                print("%d: %s " % (idx, conts[idx]))

            # write to dict
            if conts[idx] not in yunDic:
                yunDic[conts[idx]] = []
            yunDic[conts[idx]].append([sheng, yun, note])

            # write to categorical dict
            if yunCat not in yunCatDic:
                yunCatDic[yunCat] = []
            if note != '':
                yunCatDic[yunCat].append(conts[idx] + '[' + note + ']')
            else:
                yunCatDic[yunCat].append(conts[idx])

            if idx < start:
                idx = start + 1
            else:
                idx += 1
        print()
    return yunDic, yunCatDic


if __name__ == '__main__':
    fName = checkRawFile(sys.argv)
    oriDic = readRawFile(fName)
    with open("./data/oriYunDict.json", 'w+', encoding='utf-8') as oriDicFile:
        oriDicFile.write(json.dumps(oriDic, ensure_ascii=False))

    baseDic, catDic = genDict(oriDic)
    with open("./data/baseCharDict.json", 'w+', encoding='utf-8') as baseDicFile:
        baseDicFile.write(json.dumps(baseDic, ensure_ascii=False))

    with open("./data/categoricalDict.json", 'w+', encoding='utf-8') as catDicFile:
        catDicFile.write(json.dumps(catDic, ensure_ascii=False))
