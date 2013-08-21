import pygame, sys, numpy
from pygame.locals import *

size=width,height=500,500
showwalk=True


pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SRW')
timer  = pygame.time.Clock()
dt     = 9


# Fill background with white
background = pygame.Surface(size)
background = background.convert()
background.fill((0,0,0))

# Initial Position
x=[width/2,height/2]
#x,y=width/2,height/2

def Exit():
	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()
	# Save image
	fname="RandWalk"+str(numpy.random.randint(0,99999))+".jpg"
	pygame.image.save(background,fname)
	# Quit gracefully
	pygame.quit()
	sys.exit(0)

# Start walking until we hit the edge
while 0<=x[0]<width and 0<=x[1]<height:
	# Generate new steps
	xn=[]
	for i in range(2): 
		xn.append(x[i]+numpy.random.uniform(-1,1))
	#ynew=y+numpy.random.uniform(-1,1)
	# Let's try to draw an anti-aliased line
	pygame.draw.aaline(background, (255, 255, 255), x, xn, True)
	#timer.tick( dt )
	#pygame.draw.rect(background, (255, 255, 255), [xn[0]+5,xn[1]+5, 10, 10])
	#winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
	x=xn
	# Blit everything to the screen if we want to see development
	if showwalk:
		screen.blit(background, (0, 0))
		pygame.display.flip()
		#z=pygame.time.get_ticks()		
		#if pygame.font:
			#font = pygame.font.Font(None, 64)
			#text = font.render("HA", 1, (255,255,250))
			#textprov = font.render(str((z*100)%100), 1, (255,255,250))
			#textpos = text.get_rect(centerx=background.get_width()/2)
			#background.blit(textprov, textpos)
			#background.blit(text, textpos)
		# Exit gracefully if required by pressing q
	for event in pygame.event.get():
		if event.type == KEYDOWN and event.key==K_q:
			Exit()
		
Exit()