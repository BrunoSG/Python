import numpy
def arr_range(n,m,k):
	l=[]
	for i in range(k):
		l.append(0)
	for i in range(n,m):
		l[i]=1
	return l	

def mat_range(n,m,k):
	x=[]
	for i in range(k):
		x.append([0 for j in range(k)])
	for j in range(k):
		if  arr_range(n,m,k)[j]==1:
			x[j] = arr_range(n,m,k)
	return x
	
	
def degree(x):
	ret = 0
	for i in range(0,4):
		ret += grid[wrap(x[0] + di[i])][wrap(x[1] + dj[i])]
	return ret


	
	
def gambiarra(l):
	s=''
	for n in l:
		s+=str(n)
	return s	

def quadrado(*a):
	for i in a:
		for n in i:
			print gambiarra(n)
			
			
			
			
grid_size = 50
pixel_size = 10

frameRate = 30

size = [grid_size * pixel_size,grid_size * pixel_size]


p_up = 0.25
p_down = 0.25
p_left = 0.25
p_right = 0.25


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


rates=[]
grid =[[0 for i in range(grid_size * pixel_size)] for j in range(grid_size * pixel_size)]
grid2 =[[0 for i in range(grid_size * pixel_size)] for j in range(grid_size * pixel_size)]

for i in range(grid_size/2 - pixel_size, grid_size/2):
	for j in range(grid_size/2 - pixel_size, grid_size/2):
		grid2[i][j]=1
		
for i in range(2*grid_size/3, 2*grid_size/3 + pixel_size):
	for j in range(2*grid_size/3, 2*grid_size/3 +pixel_size):
		grid2[i][j]=1			


int[] di = {0, 1, 0, -1};
int[] dj = {1, 0, -1, 0};
int curFrameRate = 10;

void setup() {
  size(SQUARE_SIZE*GRID_DIMENSION, SQUARE_SIZE*GRID_DIMENSION);
  
  for (int i = (GRID_DIMENSION - 2*SQUARE_DIMENSION)/2; i < (GRID_DIMENSION)/2; i++)
    for (int j = (GRID_DIMENSION - 2*SQUARE_DIMENSION)/2; j < (GRID_DIMENSION)/2; j++)
      grid[i][j] = 1;
  
  for (int i = 2*(GRID_DIMENSION)/3; i < 2*(GRID_DIMENSION)/3 + SQUARE_DIMENSION; i++)
    for (int j = 2*(GRID_DIMENSION)/3; j < 2*(GRID_DIMENSION)/3 + SQUARE_DIMENSION; j++)
      grid[i][j] = 1;    
    
  background(0);
  frameRate(curFrameRate);
}

void draw() {
  float elapsed = 0;
  int times = 0;
  while(elapsed < 1.0/(10*curFrameRate)) {
    elapsed += simulate(calculateRates());
    times++;
  }
  print(times); print(" - "); print(elapsed); print("\n");
    
  for (int i = 0; i < GRID_DIMENSION; i++) {
    for (int j = 0; j < GRID_DIMENSION; j++) {
      if (grid[i][j] == 1) {
        fill(255, 255, 255);
      } else {
        fill(0, 0, 0);
      }
     
      rect(map(i, 0, GRID_DIMENSION, 0, height), map(j, 0, GRID_DIMENSION, 0, width), SQUARE_SIZE, SQUARE_SIZE);
    }
  }
  
  frameRate(curFrameRate);
}

int wrap(int i) {
  if (i == GRID_DIMENSION) return 0;
  if (i == -1) return GRID_DIMENSION - 1;
  return i;
}

int degree(int i, int j) {
  int ret = 0;
  for(int k = 0; k < 4; k++)
    ret += grid[wrap(i + di[k])][wrap(j + dj[k])];
  return ret;
}

def calculateRates():
	ret = 0
 	for i in range(grid_size):
		for j in range(grid_size): 
			for k in range(2):
				new_i = wrap(i + di[k])
				new_j = wrap(j + dj[k])
				delta_positive = 0        
				if grid2[i][j] != grid2[new_i][new_j]: 
					delta_positive = (grid2[i][j] - grid2[new_i][new_j]) * (degree(i, j) - degree(new_i, new_j));
					if delta_positive < 0:
						delta_positive = 0
					rates[i][j][k] = numpy.exp(-BETA * delta_positive );
					ret += rates[i][j][k];
	return ret;
		


def simulate(sumRates):
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
	return time_metropolis

	
	
	
	
	
def draw():
	elapsed = 0
	times = 0
	while elapsed < 1.0/(10*curFrameRate) : 
		elapsed += simulate(calculateRates())
		times++
    for i in range(grid_size):
		for j in range(grid_size):
			if grid2[i][j] == 1:
				fill(255, 255, 255)
			else:
				fill(0, 0, 0)
      
     
			rect(map(i, 0, GRID_DIMENSION, 0, height), map(j, 0, GRID_DIMENSION, 0, width), SQUARE_SIZE, SQUARE_SIZE);
    
	frameRate(curFrameRate)

	
	
					
print mat_range(1,4,6)+ mat_range(1,4,6)
quadrado(mat_range(1,4,6) + mat_range(1,4,6))
print simulate(10)
#quadrado(grid2)