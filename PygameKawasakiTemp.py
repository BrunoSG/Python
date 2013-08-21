import numpy, pygame, sys
from pygame.locals import *

grid_size = 20
pixel_size = 8

frameRate = 10000

size = [grid_size * pixel_size,grid_size * pixel_size]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


p_up = 0.25
p_down = 0.25
p_left = 0.25
p_right = 0.25

BETA = 10

rates=[[[0 for k in range(2)] for j in range(grid_size)] for i in range(grid_size)]
grid  =[[0 for j in range(grid_size)] for i in range(grid_size)]
grid2 =[[0 for j in range(grid_size)] for i in range(grid_size)]


#grid2[grid_size/2][grid_size/2+1]=1
		
for i in range(2*grid_size/5, 4*grid_size/5):
	for j in range(2*grid_size/5, 4*grid_size/5):
		grid2[i][j]=1		

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

def calculateRates(x):
	m = x
	ret = 0
 	for i in range(grid_size):
		for j in range(grid_size): 
			for k in range(2):
				new_i = wrap(i + di[k])
				new_j = wrap(j + dj[k])
				delta_positive = (x[i][j] - x[new_i][new_j]) * (degree(x,i, j) - degree(x,new_i, new_j) + x[i][j] - x[new_i][new_j])
				if delta_positive < 0:
					delta_positive = 0
				rates[i][j][k] = numpy.exp(-BETA * (delta_positive+2))
				ret += rates[i][j][k]
	return [rates,m,ret]

def simulate(x,sumRates):
	random_metropolis = sumRates * numpy.random.random_sample()
	#print sumRates
	#print random_metropolis
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
					tmp = x[i][j]
					x[i][j] = x[new_i][new_j]
					x[new_i][new_j] = tmp #ver a,b=b,a					
					return [x,time_metropolis]


pygame.init()


screen = pygame.display.set_mode(size)
pygame.display.set_caption('SRW')
timer  = pygame.time.Clock()

background = pygame.Surface(size)
background = background.convert()
background.fill((0,0,0))

def Exit():
	screen.blit(background, (0, 0))
	pygame.display.flip()
	# Save image
	#fname="RandWalk"+str(numpy.random.randint(0,99999))+".jpg"
	#pygame.image.save(background,fname)
	#print grid[grid_size/2][grid_size/2]
	pygame.quit()
	sys.exit(0)

if __name__ == '__main__':
#loop of interaction 	
	while 1:	
		screen.blit(background, (0, 0))
		pygame.display.flip()	
		elapsed = 0
		#times = 0
		#while elapsed < 1.0/(1000*frameRate) : 
			#elapsed += simulate(calculateRates())
			#times += 1
			#curPos = getNextPos(curPos)
		gridTemp=simulate(grid2,calculateRates(grid2)[2])[0]	
		for i in range(grid_size):
			for j in range(grid_size):
				if gridTemp[i][j]==1:
					pygame.draw.rect(background, (255, 255, 255), [pixel_size*i,pixel_size*j, pixel_size-1, pixel_size-1])
				else:
					pygame.draw.rect(background, (0, 0, 0), [pixel_size*i,pixel_size*j, pixel_size-1, pixel_size-1])
		
		grid2 = gridTemp
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


	














