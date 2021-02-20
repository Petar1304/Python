import time
import math

def tm(x):
	m = round(x // 60)
	s = round(x % 60)
	print( m, ':', s )
	print()

t = int(input('Time: '))
d = int(input('Distance: '))
v = d / t

print('200m: ') 
tm(200 / v)
print('250m: ') 
tm(250 / v)
print('300m: ') 
tm(300 / v)
print('350m: ') 
tm(350 / v)
print('500m: ') 
tm(500 / v)
print('1000m: ') 
tm(1000 / v)
