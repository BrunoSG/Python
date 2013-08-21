import numpy, pygame, sys
from pygame.locals import *

grid_size = 50
pixel_size = 10

frameRate = 60

size = [grid_size * pixel_size,grid_size * pixel_size]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


p_up = 0.25
p_down = 0.25
p_left = 0.25
p_right = 0.25

BETA = 2

rates=[]
grid  =[[0 for i in range(grid_size)] for j in range(grid_size)]
grid2 =[[0 for i in range(grid_size)] for j in range(grid_size)]

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

def flip_edge(x,i,j,k):	
	tmp = x[i][j]
	x[i][j] = x[wrap(i+di[k])][wrap(j+di[k])]
	x[wrap(i+di[k])][wrap(j+di[k])] = tmp
	
def degree(x,y):
	ret=0
	for i in range(4):
		ret+=grid[wrap(x)+di[i]][wrap(y)+dj[i]]
	return ret

def E(x):
    #Return the energy of some configuration s.
	cur_sum=0
	for i in range(grid_size):
		for j in range(grid_size):
			for k in range(2):
				cur_sum += x[i][j]*x[wrap(i+di[k])][wrap(j+dj[k])]
	return -cur_sum

def step(s, kT):
    '''Given some system configuration s and some normalized
    temperature kT, perform one step of a Metropolis method.

    Returns the energy of the new configuration.
    '''

    energy = E(s) # pre-perturbation energy
    loc=[] = random_integers(0, n-1) # pick a random location
    s[loc] = -s[loc] # flip a location.  s[loc] *= -1
    trial_energy = E(s) # post-perturbation energy
    delta_E = trial_energy - energy
    if delta_E < 0:
        # energy went down, so accept
        return trial_energy
    else:
        # the energy of the new config is higher;
        # accept with some probability
        P_accept = exp(-delta_E / kT) # probability of acceptance
        if random_sample() <= P_accept:
            # we accept the perturbation
            return trial_energy
        else:
            # we reject the perturbation
            s[loc] = -s[loc] # put it back the way we found it
            return energy

if __name__ == '__main__':
    J = 1. # half the difference between different-neighbor and same-neighbor interaction energies.
    # Uncomment the below line to simulate an antiferromagnetic system instead.
    # J = -1.
    n = 10 # number of spins in the system
    n_steps = 100 # number of steps to take
    kT = 1.0 # the (constant) value of k*T

    s = where(random_sample(size=n) < 0.5, -1, 1) # an initial random
                                                  # configuration,
                                                  # approximately half up
                                                  # and half down.

    ion() # interactive mode on, so pylab will show the plot as it runs
    # configurations will be shown as one-row images.  Hence, we need to
    # make s look 2-dimensional before we feed it to imshow by using
    # atleast_2d:
    myplot = imshow(atleast_2d(s), interpolation='nearest')
    t = title('') # start with an empty title; we'll fill this in later
    draw() # replaces show when you want the code to keep running

    from time import sleep

    for i in range(n_steps): # simulate 100 steps
        energy = step(s, kT) # perform one step of the Metropolis Monte-Carlo method.
        myplot.set_data(atleast_2d(s)) # replace the image with new data
        label = 'kT = %s, E = %s, iteration=%s' % (kT, energy, i)
        t.set_text(label) # update the title text
        sleep(0.1) # twiddle our thumbs for 0.1 second.
        draw()