import numpy, pygame, sys
from pygame.locals import *

grid_size = 10
pixel_size = 8

frameRate = 5

size = [grid_size * pixel_size,grid_size * pixel_size]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

p_up = 0.25
p_down = 0.25
p_left = 0.25
p_right = 0.25


rates=[]
gridTemp =[[0 for j in range(grid_size)] for i in range(grid_size)]
grid2 =[0 for j in range(grid_size)]
for i in range(1, 5):
	for j in range(1, 5):
		gridTemp[i][j]=1


def gambiarra(l):
	s=''
	for n in l:
		s+=str(n)
	return s	

def quadrado(*a):
	for i in a:
		for n in i:
			print gambiarra(n) 
a1=[[1,2,3,4],[1,2,3,5],[2,3,5,2]]
a2=[[1,2,3,4],[1,2,3,5],[2,3,5,1]]
a3=[[1,2,3,4],[1,2,3,5],[2,3,5,3]]
a4=[[1,2,3,4],[1,2,3,5],[2,3,5,7]]
a5=[[1,2,3,4],[1,2,3,5],[2,3,5,0]]
a=[[0 for y in range(10) ] for x in range(10) if x<20]
#quadrado(a1,a2)
#quadrado(a)			

def wrap(i):
  if i == -1:
	return grid_size - 1;
  else:
	if i == grid_size:
		return 0;
	else:
		return i		

def getNextPos(x,grid_size):
	Unif = grid_size * numpy.random.uniform(0.0,1.0)
	UnifDir = numpy.random.randint(2)
	temp_sum=0
	count=0
	for i in range(grid_size):
		while count==0:
			temp_sum += 1
			if Unif <= temp_sum:
				count=1
				if UnifDir == 1:
					tmp = x[grid_size/2][i]
					x[grid_size/2][i] = x[grid_size/2][wrap(i+1)]
					x[grid_size/2][wrap(i+1)] = tmp
				else:
					tmp = x[grid_size/2][i]
					x[grid_size/2][i] = x[grid_size/2][wrap(i-1)]
					x[grid_size/2][wrap(i-1)] = tmp
	return x

	
cur_sum=0
for i in range(grid_size):
	for j in range(grid_size):
		for k in range(2):
			cur_sum += gridTemp[i][j]* gridTemp[wrap(i+di[k])][wrap(j+dj[k])]
print -cur_sum		


