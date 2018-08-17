import plotset as ps 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def figa(pt,pIKK,pNc,pNn,pIc,pIn,pA,sample):
	plt.style.use('seaborn-dark')
	######FIGURE#########################################################################
	fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
	#####AXES######################################################################
	likk=ps.plotIKK(ax1,pt,pIKK)
	lsamp=ps.sample(ax1)
	ax1.legend((likk,lsamp),('IKK',sample),loc='upper right')
	
	lnc=ps.plotNc(ax2,pt,pNc)
	lnn=ps.plotNn(ax2,pt,pNn)
	lsamp=ps.sample(ax2)
	ax2.legend((lnc,lnn,lsamp),('Nc', 'Nn',sample),loc='upper right')

	lic=ps.plotIc(ax3,pt,pIc)
	lin=ps.plotIn(ax3,pt,pIn)
	lsamp=ps.sample(ax3)
	ax3.legend((lic,lin,lsamp),('Ic','In',sample),loc='lower right')

	la=ps.plotA(ax4,pt,pA)
	lsamp=ps.sample(ax4)
	ax4.legend((la,lsamp),('A',sample),loc='upper right')
	
	####ENVIRONMENT###############################################################
	fig1.suptitle('time development - wt0')
	wdth=np.amax(pt)
	wstep=int(wdth/10)

	ps.meanax(ax1,wdth,wstep,pt)
	ps.meanax(ax2,wdth,wstep,pt)
	ps.meanax(ax3,wdth,wstep,pt)
	ps.meanax(ax4,wdth,wstep,pt)

	fig1.tight_layout()
	plt.show()
	#ps.save(fig1)
	plt.close()
	############################################################################## 

def figb(pte,pSe,pIKKe,pNne,pIce,pAe,sample):
	plt.style.use('seaborn-dark')
	######FIGURE##########################################################################
	fig2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
	######AXES######################################################################
	likk=ps.plotIKK(ax1,pte,pIKKe)
	ls=ps.plotS(ax1,pte,pSe)
	lsamp=ps.sample(ax1)
	ax1.legend((likk,ls,lsamp),('IKK','S',sample),loc='upper left')

	lnn=ps.plotNn(ax2,pte,pNne)
	ls=ps.plotS(ax2,pte,pSe)
	lsamp=ps.sample(ax1)
	ax2.legend((lnn,ls,lsamp),( 'Nn','S',sample),loc='upper left')

	lic=ps.plotIc(ax3,pte,pIce)
	ls=ps.plotS(ax3,pte,pSe)
	lsamp=ps.sample(ax1)
	ax3.legend((lic,ls,lsamp),('Ic','S',sample),loc='upper left')

	la=ps.plotA(ax4,pte,pAe)
	ls=ps.plotS(ax4,pte,pSe)
	lsamp=ps.sample(ax1)
	ax4.legend((la,ls,lsamp),('A','S',sample),loc='upper left')

	
	####ENVIRONMENT###############################################################
	fig2.suptitle('time development - activation')
	wdth=np.amax(pte)
	wstep=int(wdth/10)

	ps.meanax(ax1,wdth,wstep,pte)
	ps.meanax(ax2,wdth,wstep,pte)
	ps.meanax(ax3,wdth,wstep,pte)
	ps.meanax(ax4,wdth,wstep,pte)

	fig2.tight_layout()
	plt.show()
	#ps.save(fig2)
	plt.close()
	############################################################################## 

def phaseplot1(x,namex,y,namey,w):
	plt.style.use('seaborn-dark')
	######FIGURE##########################################################################
	fig, ax = plt.subplots(nrows=1, ncols=1)

	ps.phaseplot(ax,x, y, w, cm.YlGnBu_r)

	ps.phaseax(ax, namex, namey)

	fig.tight_layout()
	plt.show()
	#ps.save(fig)
	plt.close()
	##############################################################################

def phaseplot2(x,namex,y,namey,w,probe):
	plt.style.use('seaborn-dark')
	######FIGURE##########################################################################
	fig, ax = plt.subplots(nrows=1, ncols=1)

	ps.phasefull(ax,x, y, w, cm.YlGnBu_r,probe)

	ps.phaseax(ax, namex, namey)

	fig.tight_layout()
	plt.show()
	#ps.save(fig)
	plt.close()
	##############################################################################