import numpy, pygame, sys
from pygame.locals import *


def gambiarra(l):
	s=''
	for n in l:
		s+=str(n)
	return s	

def quadrado(*a):
	for i in a:
		for n in i:
			print gambiarra(n)
			


grid_size=40
BETA = 1
rates=[[[0 for k in range(2)] for j in range(grid_size)] for i in range(grid_size)]
grid2 =[[0 for j in range(grid_size)] for i in range(grid_size)]

for i in range(2*grid_size/4):
	for j in range(2*grid_size/4):
		grid2[i][j]=1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def wrap(i):
	#i = i % grid_size
	if i == -1:
		return grid_size - 1
	else:
		if i >= grid_size:
			return i - grid_size
		else:
			return i


def degree(m,x,y):
	ret=0
	for k in range(4):
		ret += m[wrap(x+di[k])][wrap(y+dj[k])]
	return ret

def deltaM(i,j,k,m):
	temp =  (m[wrap(i+di[k])][wrap(j+dj[k])]-m[i][j])*(degree(m,wrap(i+di[k]),wrap(j+dj[k]))-degree(m,i,j)+m[i+di[k]][j+dj[k]]-m[i][j])	
	if temp < 0:
		return 0
	else:
		return temp
				


def calculateRates(z,grid_size,r):
	n=[[0 for j in range(grid_size)] for i in range(grid_size)]
	ret = 0
 	for i in range(grid_size):
		for j in range(grid_size): 
			for k in range(2):
				temp=-BETA * deltaM(i,j,k,z)
				r[i][j][k] = numpy.exp(temp)
				ret += rates[i][j][k]
			n[i][j]= degree(z,i,j)	
	return n


#l= calculateRates(grid2)[2]
temp=[[0 for j in range(grid_size)] for i in range(grid_size)]
for i in range(grid_size):
	for j in range(grid_size):
		temp[i][j]=degree(grid2, i,j)
#			degree(grid2, i + di[k], j + dj[k])
#	print l[i]
#			for k in range(2):
#				print rates[i][j][k]
quadrado(calculateRates(grid2,grid_size,rates))

