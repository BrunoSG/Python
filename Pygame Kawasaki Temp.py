import numpy, pygame, sys
from pygame.locals import *

grid_size = 30
pixel_size = 10

frameRate = 5

size = [grid_size * pixel_size,grid_size * pixel_size]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


p_up = 0.25
p_down = 0.25
p_left = 0.25
p_right = 0.25

BETA = 0.01

rates=[[[0 for k in range(2)] for j in range(grid_size)] for i in range(grid_size)]
grid  =[[0 for j in range(grid_size)] for i in range(grid_size)]
grid2 =[[0 for j in range(grid_size)] for i in range(grid_size)]

for i in range((grid_size)/4, 2*grid_size/4):
	for j in range((grid_size)/4, 2*grid_size/4):
		grid2[i][j]=1
		
#for i in range(3*grid_size/5, 4*grid_size/5):
#	for j in range(3*grid_size/5, 4*grid_size/5):
#		grid2[i][j]=1		

def wrap(i):
  i = i % grid_size
  return i
		
def degree(m,x,y):
	ret=0
	for k in range(4):
		ret += m[wrap(x+di[k])][wrap(y+dj[k])]
	return ret

curPos =[]

#initial position
#for i in range(2):
#	curPos.append(grid_size/2)
#grid[curPos[0]][curPos[1]]=1

def calculateRates(grid2):
	m = grid2
	ret = 0
 	for i in range(grid_size):
		for j in range(grid_size): 
			for k in range(2):
				new_i = wrap(i + di[k])
				new_j = wrap(j + dj[k])
				delta_positive = (grid2[i][j] - grid2[new_i][new_j]) * (degree(grid2,i, j) - degree(grid2,new_i, new_j) + grid2[i][j] - grid2[new_i][new_j])
				if delta_positive < 0:
					delta_positive = 0
				rates[i][j][k] = numpy.exp(-BETA * delta_positive)
				ret += rates[i][j][k]
	return [rates,m,ret]

def simulate(grid2,sumRates):
	random_metropolis = sumRates * numpy.random.random_sample()
	time_metropolis = numpy.random.exponential(1/sumRates)
	#Parte facilmente simplificavel
	cur_sum = 0 
	for i in range(grid_size):
		for j in range(grid_size): 
			for k in range(2):
				cur_sum += rates[i][j][k]
				if cur_sum >= random_metropolis:
					new_i = wrap(i + di[k])
					new_j = wrap(j + dj[k])
					tmp = grid2[i][j]
					grid2[i][j] = grid2[new_i][new_j]
					grid2[new_i][new_j] = tmp
	return [grid2,time_metropolis]


pygame.init()


screen = pygame.display.set_mode(size)
pygame.display.set_caption('SRW')
timer  = pygame.time.Clock()

background = pygame.Surface(size)
background = background.convert()
background.fill((0,0,0))

def getNextPos(x):
	Unif = numpy.random.uniform(0.0,1.0)
	if Unif <= p_left:
		x[0]-=1
	else:
		if Unif <= p_right + p_left:
			x[0] += 1
		else:
			if Unif <= p_down + p_right + p_left:
				x[1] -= 1
			else:
				if Unif <= p_up + p_down + p_right + p_left:
					x[1] += 1
	for j in range(2):
		x[j] = wrap(x[j])
	return x


def Exit():
	screen.blit(background, (0, 0))
	pygame.display.flip()
	# Save image
	#fname="RandWalk"+str(numpy.random.randint(0,99999))+".jpg"
	#pygame.image.save(background,fname)
	print grid[grid_size/2][grid_size/2]
	pygame.quit()
	sys.exit(0)

#loop of interaction 	
while 1:	
	screen.blit(background, (0, 0))
	pygame.display.flip()	
	elapsed = 0
	#times = 0
	#while elapsed < 1.0/(1000*frameRate) : 
	#	elapsed += simulate(calculateRates())
		#times += 1
		#curPos = getNextPos(curPos)
	gridTemp=simulate(grid2,calculateRates(grid2)[2])[0]	
	for i in range(grid_size):
		for j in range(grid_size):
			if gridTemp[i][j]==1:
				pygame.draw.rect(background, (255, 255, 255), [pixel_size*i,pixel_size*j, pixel_size-1, pixel_size-1])
			else:
				pygame.draw.rect(background, (0, 0, 0), [pixel_size*i,pixel_size*j, pixel_size-1, pixel_size-1])
	
	screen.blit(background, (0, 0))
	pygame.display.flip()
	timer.tick( frameRate )
	
	#new position
	#pygame.draw.rect(background, (255, 255, 255), [pixel_size*curPos[0],pixel_size*curPos[1], pixel_size-1, pixel_size-1])
		
	#curPos = getNextPos(curPos)
	#grid[curPos[0]][curPos[1]] += 1
	#pygame.draw.rect(background, (255, 0, 0), [pixel_size*curPos[0],pixel_size*curPos[1], pixel_size-1, pixel_size-1])
	
	#for i in range(7):
	#	pygame.draw.rect(background, (255, 255, 255), [pixel_size*(curPos[0]+i*(2*numpy.random.randint(0,2)-1)),pixel_size*(curPos[1]-i*(2*numpy.random.randint(0,2)-1)), pixel_size, pixel_size])
	#pygame.draw.rect(background, (0, 255, 0), [pixel_size*(curPos[0] + 2*numpy.random.randint(0,2)-1),pixel_size*(curPos[1] + 2*numpy.random.randint(0,2)-1), pixel_size, pixel_size])
	#screen.blit(background, (0, 0))
	#pygame.display.flip()
	for event in pygame.event.get():
		if event.type == KEYDOWN and event.key==K_q:
			Exit()
	
Exit()			


	














