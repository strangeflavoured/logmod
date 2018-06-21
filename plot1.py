import plotset as ps 
import matplotlib.pyplot as plt
import numpy as np

#PLOTTING###################################################################################
plt.style.use('seaborn-dark')

def figa(pt,pIKK,pNc,pNn,pIc,pIn,pA,sample):
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

	ps.plotax(ax1,wdth,wstep,pt)
	ps.plotax(ax2,wdth,wstep,pt)
	ps.plotax(ax3,wdth,wstep,pt)
	ps.plotax(ax4,wdth,wstep,pt)

	fig1.tight_layout()
	plt.show()
	#ps.save(fig1)
	plt.close()

def figb(pte,pSe,pIKKe,pNne,pIce,pAe,sample):
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

	fig2.suptitle('time development - activation')
	wdth=np.amax(pte)
	wstep=int(wdth/10)

	ps.plotax(ax1,wdth,wstep,pte)
	ps.plotax(ax2,wdth,wstep,pte)
	ps.plotax(ax3,wdth,wstep,pte)
	ps.plotax(ax4,wdth,wstep,pte)

	fig2.tight_layout()
	plt.show()
	#ps.save(fig2)
	plt.close()