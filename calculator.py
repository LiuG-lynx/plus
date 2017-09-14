#!/usr/bin/env python3

import sys
def shuru(a):
    del a[0]
    b = ':'.join(a).split(':')
    m = b[::2]
    n = b[1::2]
    c = []
    for i in n:
        c.append(int(i));
    n =c
    return m,n 
def jisuan(n,m):
	x = []
	for i in n:
		if i < 0:
			raise ValueError()
		l = (float(i) * 0.165)
		b = i - 3500
		d = i - 3500 - l
		if b <= 0:
			c = 0
		elif b <= 1500:
			c = (d * 0.03)
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
		x.append(i - l - c)
        #print(x)
	    #print(m)
	    #print(format(float(x), ".2f"))
	for j in range(len(m)):
	    print('{}:{:.2f}'.format(m[j],x[j]))



if __name__ == '__main__':
	try:
	    m,n = shuru(sys.argv)
	    jisuan(n,m)
	except ValueError:
		print("Parameter Error")
	except IndexError:
		print("Parameter Error")
	

