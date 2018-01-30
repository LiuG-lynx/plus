#!/usr/bin/env python3

import sys
import getopt
import configparser
from datetime import date,datetime
from multiprocessing import Process,Queue
from collections import OrderedDict

def jc1():
    opts,args = getopt.getopt(sys.argv[1:],'-h-c:-d:-C:-o:',['help'])
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")
            exit()
        if opt_name in ('-c'):
            valcfg = opt_value
        if opt_name in ('-d'):
            valuser  = opt_value
        if opt_name in ('-o'):
            valgz = opt_value
        if opt_name in ('-C'):
            valsection = opt_value.upper()     
# chushihua
    update_config_parser = configparser.ConfigParser()
    update_config_parser.read(valcfg)
    sectioncfg = update_config_parser[valsection]
    diccfg = OrderedDict()
    diccfg['JiShuL'] = float(sectioncfg['JiShuL'])
    diccfg['JiShuH'] = float(sectioncfg['JiShuH'])
    diccfg['YangLao'] = float(sectioncfg['YangLao'])
    diccfg['YiLiao'] = float(sectioncfg['YiLiao'])
    diccfg['ShiYe'] = float(sectioncfg['ShiYe'])
    diccfg['GongShang'] = float(sectioncfg['GongShang'])
    diccfg['ShengYu'] = float(sectioncfg['ShengYu'])
    diccfg['GongJiJin'] = float(sectioncfg['GongJiJin'])
    cfg = valcfg
    user = valuser
    filegz = valgz
    user1 = open(user, 'r')
    User = user1.read()
    listuser = User.split('\n')
    listuser.remove('')
    splitlistuser = ','.join(listuser).split(',')
    listid = splitlistuser[::2]
    listshuiq = splitlistuser[1::2]
    t = []
    for i in listshuiq:
        t.append(int(i))
    listshuiq = t
    user1.close()
    
    cfg1  = open(cfg, 'r')
    cfg1.close()
    quequeid.put(listid)
    quequeshuiq.put(listshuiq)
    quequecfg.put(diccfg)
    quequefile.put(filegz)

def jc2():
    listid = quequeid.get()
    listshuiq = quequeshuiq.get()
    diccfg = quequecfg.get()
    jieguo = []
    shebao = []
    geshui = []
    shuihou = []
    he = diccfg['YangLao'] + diccfg['YiLiao'] + diccfg['ShiYe'] + diccfg['GongShang'] + diccfg['ShengYu'] + diccfg['GongJiJin']
    for i in range(len(listshuiq)):
        if listshuiq[i] < diccfg['JiShuL']:
            shebao.append(diccfg['JiShuL'] * he)
        elif listshuiq[i] > diccfg['JiShuH']:
            shebao.append(diccfg['JiShuH'] * he)
        else:
            shebao.append(listshuiq[i] * he)
        b = listshuiq[i] - 3500
        d = listshuiq[i] - shebao[i] - 3500
        if b <= 0:
            c = 0
        elif b <= 1500:
            c = d * 0.03
        elif b <= 4500 and b > 1500:
            c = (d * 0.1) - 105
        elif b <= 9000 and b > 4500:
            c = (d * 0.2) - 555
        elif b <= 35000 and b > 9000:
            c = (d * 0.25) - 1005
        elif b <= 55000 and b > 35000:
            c = (d * 0.3) - 2755
        elif b <= 80000 and b > 55000:
            c = (d * 0.35) - 5505
        elif b > 80000:
            c = (d * 0.45) - 13505
        geshui.append(c)
        shuihou.append(listshuiq[i] - shebao[i] - geshui[i])
        time = datetime.now()
        time1 = datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
        jieguo.append('{},{},{:.2f},{:.2f},{:.2f}'.format((listid[i]),(listshuiq[i]),(shebao[i]),(geshui[i]),(shuihou[i])))
    quequejg.put(jieguo)
    quequetime.put(time1)
def jc3():
    file1 = quequefile.get()
    jg = quequejg.get()
    time = quequetime.get()
    with open(file1, 'w') as file:
        for i in range(len(jg)):
            file.write(jg[i] +','+time +'\n')
def main():
    Process(target=jc1).start()
    Process(target=jc2).start()
    Process(target=jc3).start()
if  __name__ == '__main__':
    quequeid = Queue()
    quequeshuiq =Queue()
    quequecfg = Queue()
    quequefile = Queue()
    quequejg = Queue()
    quequetime = Queue()
    main()
