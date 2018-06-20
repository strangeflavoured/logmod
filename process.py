import numpy as np
def length(a,b):
	length=[]
	for i in range(0,b):
		length.append(len(a[i]))
	w=np.amax(length)
	return w

def time(a):
	t=[]
	for i in range(0,a):
		t.append(i)
	t=np.array(t)
	return t

#SUM auffullen damit alle gleiche Länge haben
def fill(b,w,n):
	for j in range(0,n):
		a=b[j]
		f=len(a)

		if f<w:
			for k in range(f,w):
				a=np.concatenate((a,[a[f-1]]))
			b[j]=a
	return b

#mittelwertarray
def mearr(a,d,n,w):
	k=0
	P=[]
	while k<d:
		j=0
		S=[]
		while j<w:
			R=[]
			for i in range(0,n):
				R.append(a[i,j,k])
				#R: alle zust d variable zum zeitpunkt t (aus allen durchl.): [x0 x0' x0''...]
			S.append(sum(R)/n)
			#S: mittelwert der variable bei jedem Zeitpunkt: [x0 x1 x2...]
			j+=1
		S=np.array(S)
		P.append(S)
		#P: mittelwerte aller variablen zu jedem zeitpunkt: [[x0 x1 x2...][y0 y1...]...]
		k+=1		
	P=np.stack(P)
	return P

def fuse(a,b,n):	
	eSUM=[]
	for i in range(0,n):
		a=np.concatenate((a[i],b[i]))
		eSUM.append(a)
	eSUM=np.stack(eSUM)
	return eSUM

def save():
	save=str(input('save as: '))
	if save not in ('0', 'NO', 'no', 'No', 'nein', 'NEIN', 'Nein','n', 'N', '', ' ','q', 'Q','quit', 'Quit'):
		fig.savefig(save, dpi=500)#fullscreen
		s=save+'small'
		fig.savefig(s, dpi=150)
