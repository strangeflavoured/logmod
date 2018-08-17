import numpy as np
def cb(a,b,c):
	if np.array_equal(a,b)==True and np.array_equal(a,c)==True:
		BREAK=True
		steady=True
		newstate=0
	elif np.array_equal(a,b)==True and np.array_equal(a,c)==False:				
		newstate=np.array(b)
		steady=True
		BREAK=False
	else:
		steady=False
		BREAK=False
		newstate=0
	return (BREAK,steady,newstate)
	

#identifizierung upzudatender variablen
def selup(a,b,c):
	global L
	L=[]
	for i in range(0,c):
		if a[i]==b[i]:
			L.append(0)
		else:
			L.append(1)
	L=np.array(L)
	return L

#bestimmung upzudatender variable (random)
def rupdate(a):
	l=[]
	for i in range(0,int(len(a))):
		if a[i]!=0:
			l.append(i)			
	l=np.array(l)
	r=int(np.random.choice(l))
	return r		

#bestimmung folgezustand
def update(a,b,c,d):
	newstate=[]	
	for i in range(0,d):
		if i==c:
			newstate.append(a[c])
		else:
			newstate.append(b[i])
	newstate=np.array(newstate)
	return newstate