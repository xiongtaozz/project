# -*- coding:utf-8 -*-
import time

TIMEFORMAT = '%Y-%m-%d %X'
operate = ''


def iforead(sperate):
    s
    if sperate='r':
        s='r'
        return s
    elif sperate='w':
        s='a'
        return s
    elif sperate='exit':
        break
    else:
        continue

def openorwrite():
    


while operate != 'exit':
    operate = raw_input('Please choose your operation(r/w/exit):')
    s = ''
    if operate == 'r':
        s = 'r'
    elif operate == 'w':
        s = 'a'
    else:
        continue
    try:
        with open('record.log', s) as f:
            if operate == 'r':
                for line in f.readlines():
                    print line
            elif operate == 'w':
                text = raw_input()
                while text != 'exit':
                    f.writelines(text + '---' +
                                 time.strftime(TIMEFORMAT, time.localtime()) + '\n')
                    text = raw_input()
    except Exception, e:
        print 'Exception:' + e
