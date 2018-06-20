def ID(a):
	if a==1:
		rid=1
	else:
		rid=0
	return rid

def NOT(a):
	if a==0:
		rnot=1
	else:
		rnot=0
	return rnot

def AND(a,b):
	if a==1 and b==1:
		rand=1
	else:
		rand=0
	return rand

def OR(a,b):
	if a==1 or b==1:
		ror=1
	else:
		ror=0
	return ror

def XOR(a,b):
	if a==1 and b==0 or a==0 and b==1:
		rxor=1
	else:
		rxor=0
	return rxor