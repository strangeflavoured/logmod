from logfkt import ID, NOT, AND, OR, XOR
#S=a[0]
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
	return im