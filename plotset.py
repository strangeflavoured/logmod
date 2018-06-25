import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def meanax(a,b,c,pt):
	a.set_xlabel('time t')
	a.set_xlim(0, np.max(pt))
	a.set_ylabel('mean level')
	a.set_ylim(-0.0625,1.0625)
	a.yaxis.set_minor_locator(plt.MultipleLocator(0.0625))
	a.grid(which='major', c='gray', linewidth=0.5, linestyle='--')
	a.grid(which='minor', linewidth=0.25, linestyle=':')
	a.set_yticks(np.arange(0, 1.1, step=0.25))
	a.set_xticks(np.arange(0, b+1, step=c))

def phaseax(a,b,c):
	a.set_title('phaseplot')
	mx='mean %s' %b
	my='mean %s' %c
	a.set_xlabel(mx)
	a.set_xlim(-0.0625,1.0625)
	a.set_ylabel(my)
	a.set_ylim(-0.0625,1.0625)
	a.set_yticks(np.arange(0, 1.1, step=0.25))
	a.set_xticks(np.arange(0, 1.1, step=0.25))
	a.grid(which='major', c='gray', linewidth=0.5, linestyle='--')
	a.grid(which='minor', linewidth=0.25, linestyle=':')

def sample(a):
	handles, labels = a.get_legend_handles_labels()
	lsamp = plt.Line2D((0,1),(0,0), linewidth=1.5, linestyle='')
	return lsamp

def plotS(a,b,c):
	a.plot(b, c, linewidth=2, linestyle='--', c='g')
	handles, labels = a.get_legend_handles_labels()
	ls = plt.Line2D((0,1),(0,0), c='g', linewidth=1.5, linestyle='-')
	return ls

def plotIKK(a,b,c):
	a.plot(b, c, linewidth=1.5, c='r')
	handles, labels = a.get_legend_handles_labels()
	likk = plt.Line2D((0,1),(0,0), c='r', linewidth=1.5, linestyle='-')
	return likk

def plotNc(a,b,c):
	a.plot(b, c, linewidth=1.5, c='royalblue')
	handles, labels = a.get_legend_handles_labels()
	lnc = plt.Line2D((0,1),(0,0), c='royalblue', linewidth=1.5, linestyle='-')
	return lnc

def plotNn(a,b,c):
	a.plot(b, c, linewidth=1.5, c='navy')
	handles, labels = a.get_legend_handles_labels()
	lnn = plt.Line2D((0,1),(0,0), c='navy', linewidth=1.5, linestyle='-')
	return lnn

def plotIc(a,b,c):
	a.plot(b, c, linewidth=1.5, c='purple')
	handles, labels = a.get_legend_handles_labels()
	lic = plt.Line2D((0,1),(0,0), c='purple', linewidth=1.5, linestyle='-')
	return lic

def plotIn(a,b,c):
	a.plot(b, c, linewidth=1.5, c='orchid')
	handles, labels = a.get_legend_handles_labels()
	lin = plt.Line2D((0,1),(0,0), c='orchid', linewidth=1.5, linestyle='-')
	return lin

def plotA(a,b,c):
	a.plot(b, c, linewidth=1.5, c='y')
	handles, labels = a.get_legend_handles_labels()
	la = plt.Line2D((0,1),(0,0), c='y', linewidth=1.5, linestyle='-')
	return la

def phaseplot(a,x,y,w,colourmap):
	colour=colourmap(np.linspace(0, 1, w))
	a.plot(x,y, '-', linewidth=1)
	for col in range(0,w):
		a.plot(x[col],y[col], 'o', c=colour[col])

def phasefull(a,x,y,w,colourmap,probe):
	colour=colourmap(np.linspace(0, 1, w))
	for i in range(0,probe):
		a.plot(x[i],y[i], '-', linewidth=1)
		for col in range(0,w):
			a.plot(x[:,col],y[:,col], 'o', c=colour[col])	

def save(fig):
	save=str(input('save as: '))
	if save not in ('0', 'NO', 'no', 'No', 'nein', 'NEIN', 'Nein','n', 'N', '', ' ','q', 'Q','quit', 'Quit'):
		fig.savefig(save, dpi=500)#fullscreen
		s=save+'small'
		fig.savefig(s, dpi=150)
