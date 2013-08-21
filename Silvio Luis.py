def SilvioLuis(n,l):
	if n>=l:
		print 'ele'
	else:
		print 'foi'
SilvioLuis(8,1)	

a = [1,2,3,4,5,6,7,8,9,10]
b = [2*x for x in a if x % 2 == 0]
print b
for n in a:
	SilvioLuis(n,len(a))

