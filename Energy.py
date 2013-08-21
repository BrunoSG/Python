import numpy

grid_size = 20
di = [0, 1, 0, -1] #coordinates
dj = [1, 0, -1, 0]
ddi = [1, -1, -1, 1] #diagonal directions
ddj = [1, 1, -1, -1]
dcompi = [1,1,0,-1,-1,-1,0,1] #all directions
dcompj = [0,1,1,1,0,-1,-1,-1]

def wrap(i):
	i = i % grid_size
	return i
	
initial =[[0 for j in range(grid_size)] for i in range(grid_size)]
		
for i in range(2*grid_size/5, 4*grid_size/5):
	for j in range(2*grid_size/5, 4*grid_size/5):
		initial[i][j]=1		

def energy (x):
	cur_sum1 = 0
	cur_sum2 = 0
	for l in range(grid_size):
		for m in range(grid_size):
			for k in range(4):
				cur_sum1 += x[l][m]* x[wrap(l+dcompi[k])][wrap(m+dcompj[k])]
				cur_sum2 += x[l][m]* x[wrap(l+di[k])][wrap(m+dj[k])]
	return [-cur_sum1,-cur_sum2/2]	
	
print energy(initial)	