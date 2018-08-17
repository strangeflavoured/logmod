import numpy as np

import modell as mod 
import initial as init
import sym 
import process as prc
from event import e1,e2
from plot1 import figa,figb,phaseplot1,phaseplot2

#######INITIATION#######################################################################################
d=mod.d

ina=input('init. cond.: ')
inb=input('sim. cond.: ')
event=int(input('how many events? '))

incd=init.init(ina,inb)

total=False
if ina in ('all','all0','all1'):
	total=True

if total==True:	
	INCD=incd[0]
	n=INCD.shape[0]
	N=incd[1][0]
	event=1
else:		
	n=incd[1][0]
	N=1
	
probe=n*N	
sample='n={}*{}'.format(n,N)
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

SUM=np.stack(SUM)#shape=(n,w,d)

P=prc.mearr(SUM,d,n,w)

pS=np.array(P[0])
pN=np.array(P[1])
pI=np.array(P[2])
pK=np.array(P[3]+P[4])
pA=np.array(P[5])

###########################################################################################


#######EVENT###############################################################################
eSUM=SUM
if event>0:
	ee=1	
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
		ee+=1
		eSUM=prc.fuse(eSUM,SUMe,n)#shape=(n,w,d)	
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
phaseplot1(pNn,'Nn',pIc,'Ic',w)
#phaseplot1(pNne,'Nn',pIce,'Ic',w)
#phaseplot2(SUM[:,:,2], 'Nn',SUM[:,:,3],'Ic',w,probe)

if event>0:
	figb(pte,pSe,pIKKe,pNne,pIce,pAe,sample)

prc.saveres(d,event,ina,inb,w,probe,sample,pt,SUM,P,pte,eSUM,Pe)
#############################################################################################
