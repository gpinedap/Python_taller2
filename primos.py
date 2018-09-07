cat primos.py
import sys
import math
N=int(raw_input('N:'))
a=[2]
kk=0
for g in range (3,N,2):
	kk=0
	nlim=len(a)
        for j in range (2,nlim):
		if g%a[j]==0:
			kk=kk+1
			break
		if kk==0:
		a[nlim+1]=g
print (a)

