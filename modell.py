from logfkt import ID, NOT, AND, OR, XOR
#S=a[0]
#Nc=a[1]
#Nn=a[2]
#Ic=a[3]
#In=a[4]
#Ir=a[5]
#IKK=a[6]
#Ar=a[7]
#A=a[8]
#c=a[9]

d=10

def im(a):
	im=[ID(a[0]),NOT(a[3]),AND(a[1],NOT(a[4])),AND(OR(a[5],a[3]),NOT(a[6])),AND(a[3],NOT(a[2])),ID(a[2]),AND(a[0],NOT(a[8])),ID(a[2]),ID(a[7]),ID(a[2])]
	return im
