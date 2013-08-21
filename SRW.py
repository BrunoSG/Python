import random
import math
import winsound
def flip():
	i = random.randrange(0,2)
	return 2*i-1
		
def maxim(x):
	a=0
	for i in x:
		if a<i:
			a=i
	return a
def minim(x):
	a=x[0]
	for i in x:
		if a>i:
			a=i
	return a
def media(x):
	a=0
	for i in x:
		a+=i
	return a/len(x)		
def SRW(x,n):
	pos = x
	#d = len(x)
	traj=[]
	for i in range(n):
		traj.append(pos)
		pos+= flip()
		#print pos
	return traj
	
b=[]
c=[]
for i in range(20):
	a=SRW(0,100000)
	b.append(media(a))
	c.append(minim(a))
	winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
	#print a, maxim(a)
	print b,c
	
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)		