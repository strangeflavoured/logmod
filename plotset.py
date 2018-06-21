import numpy as np
import matplotlib.pyplot as plt

def plotax(a,b,c,pt):
	a.set_xlabel('time t')
	a.set_xlim(0, np.max(pt))
	a.set_ylabel('mean level')
	a.set_ylim(-0.0625,1.0625)
	a.yaxis.set_minor_locator(plt.MultipleLocator(0.0625))
	a.grid(which='major', c='gray', linewidth=0.5, linestyle='--')
	a.grid(which='minor', linewidth=0.25, linestyle=':')
	a.set_yticks(np.arange(0, 1.1, step=0.25))
	a.set_xticks(np.arange(0, b+1, step=c))

def plotS(a,b,c):
	a.plot(b, c, linewidth=2, linestyle='--', c='g')

def plotIKK(a,b,c):
	a.plot(b, c, linewidth=1.5, c='r')

def plotNc(a,b,c):
	a.plot(b, c, linewidth=1.5, c='g')

def plotNn(a,b,c):
	a.plot(b, c, linewidth=1.5, c='b')

def plotIc(a,b,c):
	a.plot(b, c, linewidth=1.5, c='m')

def plotIn(a,b,c):
	a.plot(b, c, linewidth=1.5, c='k')

def plotA(a,b,c):
	a.plot(b, c, linewidth=1.5, c='y')

def save(fig):
	save=str(input('save as: '))
	if save not in ('0', 'NO', 'no', 'No', 'nein', 'NEIN', 'Nein','n', 'N', '', ' ','q', 'Q','quit', 'Quit'):
		fig.savefig(save, dpi=500)#fullscreen
		s=save+'small'
		fig.savefig(s, dpi=150)
