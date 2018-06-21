import numpy as np
#import matplotlib.pyplot as plt
#import plotset as ps 
import modell as mod 
import initial as init
import sym 
import process as prc
from event import e1,e2
from plot1 import figa,figb

#######INITIATION#######################################################################################
d=mod.d
total='True'#input('simulate all? ')
event=1#int(input('how many events? '))
incd=init.init('all','atest')#(input('init. cond.: '),input('sim. cond.: '))

if total=='True':
	total=True
	INCD=incd[0]
	n=INCD.shape[0]
	N=10#incd[1][0]
	event=0
else:		
	n=incd[1][0]
	N=1
probe=n*N	
sample='n=%s' %probe
it=incd[1][1]#iterations pre-event
ite=incd[1][2] #iterations event 1
it2=incd[1][3] #iterations event 2
########################################################################################################

#######SIMULATION#######################################################################################
jj=0
SUM=[]
while jj<n:
	nn=0
	while nn<N:
		if total==True:
			states=[INCD[jj]]
		else:
			states=[incd[0]]
		
		ii=0
		while ii<it:

			state=states[-1]
			lstate=[]
			if ii>0:
				lstate=states[-2]
			
			image=mod.im(state)		
			
			cb=sym.cb(image,state,lstate)
		
			BREAK=cb[0]
			steady=cb[1]
			newstate=cb[2]
			
			if BREAK==True:
				break

			elif steady==False:
				
				L=sym.selup(state,image,d)
				r=sym.rupdate(L)
				newstate=sym.update(image,state,r,d)
				
			states.append(newstate)		
			ii+=1
		nn+=1
	states=np.stack(states)
	#summieren aller simulationen
	SUM.append(states)
	jj+=1

w=prc.length(SUM,n)
pt=prc.time(w)
SUM=prc.fill(SUM,w,n)

SUM=np.stack(SUM)

P=prc.mearr(SUM,d,n,w)

pS=np.array(P[0])
pNc=np.array(P[1])
pNn=np.array(P[2])
pIc=np.array(P[3])
pIn=np.array(P[4])
pIr=np.array(P[5])
pIKK=np.array(P[6])
pAr=np.array(P[7])
pA=np.array(P[8])
pc=np.array(P[9])
###########################################################################################


#######EVENT###############################################################################
if event>0:
	ee=1
	SUMMe=SUM
	while ee<=event:
		jj=0
		SUMe=[]		
		while jj<n:

			nn=0
			while nn<N:

				if ee==1:
					incde=np.array(e1(SUM,jj))
				elif ee==2:
					incde=np.array(e2(SUM,jj))

				ii=0
				states=[incde]
				while ii<ite:

					state=states[-1]
					lstate=[]
					if ii>0:
						lstate=states[-2]
					
					image=mod.im(state)		
					
					cb=sym.cb(image,state,lstate)
				
					BREAK=cb[0]
					steady=cb[1]
					newstate=cb[2]
				
					if BREAK==True:
						break
					
					if steady==False:
						
						L=sym.selup(state,image,d)
						r=sym.rupdate(L)
						newstate=sym.update(image,state,r,d)
						
					states.append(newstate)		
					ii+=1
				states=np.stack(states)#[ii,...]
				#summieren aller simulationen
				SUMe.append(states)
				nn+=1
			jj+=1	
		SUMe=np.stack(SUMe)#[[ii,...]jj,...]
		SUMMe=prc.fuse(SUMMe,SUMe,n)
		ee+=1
		
	eSUM=prc.fuse(SUM,SUMMe,n)

	we=len(eSUM[0])
	pte=prc.time(we)
	Pe=prc.mearr(eSUM,d,n,we)

	pSe=np.array(Pe[0])
	pNce=np.array(Pe[1])
	pNne=np.array(Pe[2])
	pIce=np.array(Pe[3])
	pIne=np.array(Pe[4])
	pIre=np.array(Pe[5])
	pIKKe=np.array(Pe[6])
	pAre=np.array(Pe[7])
	pAe=np.array(Pe[8])
	pce=np.array(Pe[9])
############################################################################################

figa(pt,pIKK,pNc,pNn,pIc,pIn,pA,sample)

if event>0:
	figb(pte,pSe,pIKKe,pNne,pIce,pAe,sample)