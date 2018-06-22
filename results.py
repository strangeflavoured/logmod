import _pickle as pickle
import numpy as numpy

f=open('results.pkl','rb')
pt,SUM,P,pte,eSUM,Pe,w,probe,sample=pickle.load(f)
f.close()

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