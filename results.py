import _pickle as pickle

#fid=open('results.txt','r')
#print(fid.read())
#fid.close()

f=open('results.pkl','rb')
pt,SUM,P,pte,eSUM,Pe,w,probe,sample=pickle.load(f)
f.close()
print(w)