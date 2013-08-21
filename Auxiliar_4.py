'''Very simple demonstration of applying the Metropolis method to a 1-D Ising spin model.

R.G. Erdmann, 2008

'''
from scipy import exp, atleast_2d
from numpy.random import *
from pylab import *

def E(s):
    '''Return the energy of some configuration s.

    No boundary conditions are applied to the border spins, so the
    first and last only interact with one other spin each.

    '''
    return -sum(J*s[:-1]*s[1:])

def step(s, kT):
    '''Given some system configuration s and some normalized
    temperature kT, perform one step of a Metropolis method.

    Returns the energy of the new configuration.
    '''

    energy = E(s) # pre-perturbation energy
    loc_i = numpy.random.randint(grid_size) # pick a random location
    loc_j = numpy.random.randint(grid_size)
	loc_k = numpy.random.randint(2)
	
	
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