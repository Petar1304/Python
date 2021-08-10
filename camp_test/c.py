# BIG BANG
import math
# import numpy as np

# input:
# N => number of particles
# S => half length of a square
# T => time during which particles reflect off the square
# P => probability 

n = input().split()
N = int(n[0])
S = int(n[1])
T = int(n[2])
P = float(n[3])

Px, Py, Vx, Vy = [], [], [], []
# Px, Py => position of the particle
# Vx, Vy => velocity of the particle 
for i in range(N):
	l = input().split()
	Px.append(float(l[0]))
	Py.append(float(l[1]))
	Vx.append(float(l[2]))
	Vy.append(float(l[3]))

Ta = -1
Tb = -1
Tc = -1
### test:
# N, S, T, P = 4, 277, 1, 0.12
# Px = [-36.217119, -27.862191, 3.669490, 0.643893]
# Py = [-9.968243, 16.828632, 12.710678, -6.869181]
# Vx = [-2.112002, -1.636217, 0.247598, -0.015110]
# Vy = [-0.584747, 0.972611, 0.827422, -0.399211]
###################################

def velocity_intensity(vx, vy):
	return math.sqrt(vx**2 + vy**2)

def distance_from_center(px, py):
	return math.sqrt(px**2 + py**2)


# beginning of time is when particles are closest to the center!


position = distance_from_center(Px[i], Py[i])
velocity = velocity_intensity(Vx[i], Vy[i])

Ta = round(position/velocity)

#### Тb:

all_collisions = []
total_num_of_collisions = 0

for i in range(N):
	num_of_collisions = 0
	dPx = abs(T * Vx[i])
	dPy = abs(T * Vy[i])

	# lx, ly => distance left in x and y direction before time T
	if Vx[i] >= 0:
		lx = S - Px[i]
	
	elif Vx[i] < 0:
		lx = S + Px[i]

	if Vy[i] >= 0:
		ly = S - Py[i]
	
	elif Vy[i] < 0:
		ly = S + Py[i]


	if dPx > lx:
		x = (dPx - lx) // (2 * S)
		for _ in range(int(x) + 1):
			num_of_collisions += 1
		
	if dPy > ly:
		y = (dPy - ly) // (2 * S)
		for _ in range(int(y) + 1):
			num_of_collisions += 1

	all_collisions.append(num_of_collisions) 
	total_num_of_collisions += num_of_collisions

Tb = total_num_of_collisions

##### Tc:

lost_particles = N

for i in range(N):
	a = 1
	for j in range(all_collisions[i]):
		a *= P

	lost_particles -= a


Tc = N - lost_particles
	



# output:
# Ta => (int) how many seconds ago was the beginning of time
# Tb => (int) how man many times have particles hit the sqare sides
# Tc => (float) what is expected number of remaining particles
print(Ta, Tb, Tc)


