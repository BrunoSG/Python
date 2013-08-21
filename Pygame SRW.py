import numpy, pygame, sys
from pygame.locals import *

grid_size = 30
pixel_size = 8

frameRate = 5

size = [grid_size * pixel_size,grid_size * pixel_size]


p_up = 0.25
p_down = 0.25
p_left = 0.25
p_right = 0.25


rates=[]
grid  =[[0 for i in range(grid_size * pixel_size)] for j in range(grid_size * pixel_size)]
grid2 =[[0 for i in range(grid_size * pixel_size)] for j in range(grid_size * pixel_size)]

for i in range((grid_size - 2*pixel_size)/2, grid_size/2):
	for j in range((grid_size - 2*pixel_size)/2, grid_size/2):
		grid2[i][j]=1
		
for i in range(2*grid_size/3, 2*grid_size/3 + pixel_size):
	for j in range(2*grid_size/3, 2*grid_size/3 +pixel_size):
		grid2[i][j]=1		

def wrap(i):
  i = i % grid_size
  if i == -1:
	return grid_size - 1;
  else:
	return i		
		


curPos =[]

#initial position
for i in range(2):
	curPos.append(grid_size/2)
grid[curPos[0]][curPos[1]]=1


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
	timer.tick( frameRate )
	#curPos = getNextPos(curPos)
	pygame.draw.rect(background, (255, 0, 0), [pixel_size*curPos[0],pixel_size*curPos[1], pixel_size-1, pixel_size-1])
	
	screen.blit(background, (0, 0))
	pygame.display.flip()
	timer.tick( frameRate )
	
	#new position
	pygame.draw.rect(background, (255, 255, 255), [pixel_size*curPos[0],pixel_size*curPos[1], pixel_size-1, pixel_size-1])
		
	curPos = getNextPos(curPos)
	grid[curPos[0]][curPos[1]] += 1
	pygame.draw.rect(background, (255, 0, 0), [pixel_size*curPos[0],pixel_size*curPos[1], pixel_size-1, pixel_size-1])
	
	#for i in range(7):
	#	pygame.draw.rect(background, (255, 255, 255), [pixel_size*(curPos[0]+i*(2*numpy.random.randint(0,2)-1)),pixel_size*(curPos[1]-i*(2*numpy.random.randint(0,2)-1)), pixel_size, pixel_size])
	#pygame.draw.rect(background, (0, 255, 0), [pixel_size*(curPos[0] + 2*numpy.random.randint(0,2)-1),pixel_size*(curPos[1] + 2*numpy.random.randint(0,2)-1), pixel_size, pixel_size])
	screen.blit(background, (0, 0))
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == KEYDOWN and event.key==K_q:
			Exit()
	
Exit()			


	














