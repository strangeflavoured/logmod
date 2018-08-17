from logfkt import ID, NOT, AND, OR, XOR
#S=a[0]
<<<<<<< HEAD
#N=a[1]
#I=a[2]
#K1=a[3]
#K2=a[4]
#A=a[5]


d=6

def im(a):
	im=[ID(a[0]),
	NOT(a[2]),
	OR(NOT(OR(a[3],a[4])),AND(a[1],NOT(a[4]))),
	AND(a[0],a[5]),
	AND(a[0],NOT(a[5])),
	ID(a[1])]
=======
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
>>>>>>> cfa72ea850d2ebfbd1c0c14bc8d61fe5639dc18d
	return im
