#initial conditions associated with modell.py

import itertools
import numpy as np

All=np.array(list(itertools.product([0,1], repeat=10)))
all0=np.insert(np.array(list(itertools.product([0,1], repeat=9))),0,0,axis=1)
all1=np.insert(np.array(list(itertools.product([0,1], repeat=9))),0,1,axis=1)

#initial conditions
AB={'wt0':[0,0,0,0,0,0,0,0,0,0], 'wt1':[1,0,0,1,1,0,0,0,0,0],'all':All,'all0':all0,'all1':all1}

#number, iterations

nit={'test':[10,20,20,20],'normal':[1000,100,100,100], 'vacc':[1000000,100,100,100], 'acc':[10000,100,100,100],
'snormal':[1000,50,50,50], 'svacc':[1000000,50,50,50], 'sacc':[10000,50,50,50],
'lnormal':[1000,500,500,500], 'lvacc':[1000000,500,500,500], 'lacc':[10000,500,500,500],
'atest':[1,20,20,20],'anormal':[100,50,50,50], 'avacc':[10000,100,100,100], 'aacc':[1000,100,100,100]}

def init(a,b):
	init=[np.array(AB[str(a)]),np.array(nit[str(b)])]
	return init

