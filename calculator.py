#!/usr/bin/env python3

import sys
import configparser

class UserData(object):
	def __init__(self,data):
		self._data = data
	def get_data(self):
		return self._data
	def set_data(self,Value):
		set_data = Value
	def shuru(self):
		a = self.get_data().split('\n')
		b = list(a)
		b.remove('')
		c = ','.join(b).split(',')
		m = c[::2]
		n = c[1::2]
		t = []
		for i in n:
			t.append(int(i))
		n = t
		return m,n
class Config(object):
	def __init__(self,cfg):
		self._cfg = cfg
	def get_cfg(self):
		return self._cfg
	def set_cfg(self,Value):
		set_cfg = Value
	def shuru(self):
		fr = open(cfg,'r')
		dic = {}
		keys = []
		for line in fr:
			v = line.strip().split(' = ')
			dic[v[0]] = float(v[1])
		fr.close()
		return dic

file1 = sys.argv[4]
y = open(file1)
f = y.read()
y.close()
cfg = sys.argv[2]

user = UserData(f)
m,n = user.shuru()

config = Config(cfg)
dic = config.shuru()

filename = sys.argv[6]
jieguo = []
shebao = []
x = []
shuihou = []
he = dic['YangLao'] + dic['YiLiao'] + dic['ShiYe'] + dic['GongShang'] + dic['ShengYu'] + dic['GongJiJin']
for i in range(len(n)):
	if n[i] < dic['JiShuL']:
	    shebao.append(dic['JiShuL'] * he)
	elif n[i] > dic['JiShuH']:
            shebao.append(dic['JiShuH'] * he)
	else:
            shebao.append(n[i] * he)	
	b = n[i] - 3500
	d = n[i] - shebao[i] -3500
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
	elif b <= 55000 and b >35000:
		c = (d * 0.3) - 2755
	elif b <= 80000 and b > 55000:
		c = (d * 0.35) - 5505
	elif b > 80000:
		c = (d * 0.45) - 13505
	x.append(c)
	shuihou.append(n[i]-shebao[i]-x[i])
	jieguo.append('{},{},{:.2f},{:.2f},{:.2f}'.format((m[i]),n[i],shebao[i],x[i],shuihou[i]))
with open(filename,'w') as file:
	for i in range(len(jieguo)):
		file.write(jieguo[i] + '\n')
