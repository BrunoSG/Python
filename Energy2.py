import numpy

class domain:
	grid_size = 30
	di = [0, 1, 0, -1]
	dj = [1, 0, -1, 0]
	p_up = 0.25
	p_down = 0.25
	p_left = 0.25
	p_right = 0.25
	def wrap(i):
		i = i % grid_size
		return i
	

initial =[[0 for j in range(domain.grid_size)] for i in range(domain.grid_size)]
		
for i in range(2*domain.grid_size/5, 4*domain.grid_size/5):
	for j in range(2*domain.grid_size/5, 4*domain.grid_size/5):
		initial[i][j]=1		
			
def H(x):
    cur_sum=0
	for i in range(domain.grid_size):
		for j in range(domain.grid_size):
			for k in range(2):
				cur_sum += x[i][j]*x[domain.wrap(i+domain.di[k])][domain.wrap(j+domain.dj[k])]
	return -cur_sum	

print H(initial)	