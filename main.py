import numpy as np
import matplotlib.pyplot as plt
import plotset as ps 
import modell as mod 
import initial as init
import sym 
import process as prc
from event import e1

d=mod.d
#INITIAL CONDITIONS, SIMULATION SETTINGS#################################################################
incd=init.init('wt0','test')#(input('init. cond.: '),input('sim. cond.: '))

n=incd[1][0]
sample='n=%s' %n
it=incd[1][1]#iterations pre-event
ite=incd[1][2] #iterations event 1
it2=incd[1][3] #iterations event 2

jj=0
SUM=[]
while jj<n:
	
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



#######EVENT###############################################################################
jj=0
SUMe=[]
while jj<n:

	incd=np.array(e1(SUM,jj))
	states=[incd]
	
	ii=0
	BREAK=False
	while ii<ite:

		state=states[-1]
		lstate=[]
		if ii>0:
			lstate=states[-2]
		
		print(state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8],state[9])
###########OUT##########################################################################################
##1 0 0 1 1 0 0 0 0 0
##Traceback (most recent call last):
##  File "main.py", line 96, in <module>
##    print(state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8],state[9])
##TypeError: 'int' object is not subscriptable
#########################################################################################################
		image=mod.im(state)		
###########OUT##########################################################################################
##Traceback (most recent call last):
##  File "main.py", line 104, in <module>
##    image=mod.im(state)		
##  File "modell.py", line 16, in im
##    im=[ID(a[0]),NOT(a[3]),	AND(a[1],NOT(a[4])),AND(OR(a[5],a[3]),NOT(a[6])),AND(a[3],NOT(a[2])),ID(a[2]),AND(a[0],NOT(a[8])),ID(a[2]),ID(a[7]),ID(a[2])]
##TypeError: 'int' object is not subscriptable
##########################################################################################################				
		sym.cb(image,state,lstate)
		if BREAK==True:
			break
		
		if steady==False:
			
			sym.selup(state,image,d)
			sym.rupdate(L)
			sym.update(image,state,r,d)
			
		states.append(newstate)		
		ii+=1
	states=np.stack(states)
	#summieren aller simulationen
	SUMe.append(states)
	jj+=1	
SUMe=np.stack(SUMe)

eSUM=prc.fuse(SUM,SUMe,n)

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


#PLOTTING###################################################################################
plt.style.use('seaborn-dark')
######FIGURE#########################################################################
fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
#####AXES######################################################################
ps.plotIKK(ax1,pt,pIKK)
ps.plotNc(ax2,pt,pNc)
ps.plotNn(ax2,pt,pNn)
ps.plotIc(ax3,pt,pIc)
ps.plotIn(ax3,pt,pIn)
ps.plotA(ax4,pt,pA)

#####LEGEND####################################################################
handles, labels = ax1.get_legend_handles_labels()
l1 = plt.Line2D((0,1),(0,0), c='r', linewidth=1.5, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax1.legend((l1,l7),('IKK',sample),loc='upper right')

handles, labels = ax2.get_legend_handles_labels()
l2 = plt.Line2D((0,1),(0,0), c='g', linewidth=1.5, linestyle='-')
l3 = plt.Line2D((0,1),(0,0), c='b', linewidth=1.5, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax2.legend((l2,l3,l7),('Nc', 'Nn',sample),loc='upper right')

handles, labels = ax3.get_legend_handles_labels()
l4 = plt.Line2D((0,1),(0,0), c='m', linewidth=1.5, linestyle='-')
l5 = plt.Line2D((0,1),(0,0), c='k', linewidth=1.5, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax3.legend((l4,l5,l7),('Ic','In',sample),loc='lower right')

handles, labels = ax4.get_legend_handles_labels()
l6 = plt.Line2D((0,1),(0,0), c='y', linewidth=1.5, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax4.legend((l6,l7),('A',sample),loc='upper right')

fig1.suptitle('time development - wt0')
wdth=np.amax(pt)
wstep=int(wdth/10)

ps.plotax(ax1,wdth,wstep)
ps.plotax(ax2,wdth,wstep)
ps.plotax(ax3,wdth,wstep)
ps.plotax(ax4,wdth,wstep)

fig1.tight_layout()
plt.show()
ps.save(fig1)
plt.clf()

######FIGURE##########################################################################
fig2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
######AXES######################################################################
ps.plotIKK(ax1,pte,pIKKe)
ps.plotS(ax1,pte,pSe)
ps.plotNn(ax2,pte,pNne)
ps.plotS(ax2,pte,pSe)
ps.plotIc(ax3,pte,pIce)
ps.plotS(ax3,pte,pSe)
ps.plotA(ax4,pte,pAe)
ps.plotS(ax4,pte,pSe)

#####LEGEND#####################################################################
handles, labels = ax1.get_legend_handles_labels()
l1 = plt.Line2D((0,1),(0,0), c='r', linewidth=1.5, linestyle='-')
l8=plt.Line2D((0,1),(0,0), c='g', linewidth=2, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax1.legend((l1,l8,l7),('IKK','S',sample),loc='upper left')

handles, labels = ax2.get_legend_handles_labels()
l3 = plt.Line2D((0,1),(0,0), c='b', linewidth=1.5, linestyle='-')
l8=plt.Line2D((0,1),(0,0), c='g', linewidth=2, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax2.legend((l3,l8,l7),( 'Nn','S',sample),loc='upper left')

handles, labels = ax3.get_legend_handles_labels()
l4 = plt.Line2D((0,1),(0,0), c='m', linewidth=1.5, linestyle='-')
l8=plt.Line2D((0,1),(0,0), c='g', linewidth=2, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax3.legend((l4,l8,l7),('Ic','S',sample),loc='upper left')

handles, labels = ax4.get_legend_handles_labels()
l6 = plt.Line2D((0,1),(0,0), c='y', linewidth=1.5, linestyle='-')
l8=plt.Line2D((0,1),(0,0), c='g', linewidth=2, linestyle='-')
l7 = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
ax4.legend((l6,l8,l7),('A','S',sample),loc='upper left')

fig1.suptitle('time development - activation')
wdth=np.amax(pte)
wstep=int(wdth/10)

ps.plotax(ax5,wdth,wstep)
ps.plotax(ax6,wdth,wstep)
ps.plotax(ax7,wdth,wstep)
ps.plotax(ax8,wdth,wstep)

fig2.tight_layout()
plt.show()
ps.save(fig2)
plt.clf()
plt.close()
