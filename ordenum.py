import sys
n=int(raw_input('N: '))
a=[]
for i in range(n):
	
	c=float(raw_input('Entre numero: '))
	a.append(c)
	print (a)
for j in range (0,n-1):
	for k in range (j+1, n):
		
                if a[k] < a[j]: 
                    aux=a[j]
                    a[j]=a[k]
                    a[k]=aux
print (a)
			 
