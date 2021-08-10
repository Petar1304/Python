import numpy as np 

vec1 = np.zeros(3)
vec2 = np.zeros(3)

print("Enter first vector:")
for i in range(3):
	vec1[i] = float(input())

print("Enter second vector:")
for i in range(3):
	vec2[i] = float(input())

scal = 0
for i in range(3):
	scal += vec1[i] * vec2[i]

print(f"Skalarni proizvod: {scal}")

vec = np.zeros(3)

vec[0] = vec1[1] * vec2[2] - vec1[2] * vec2[1]
vec[1] = -1 * (vec1[0] * vec2[2] - vec1[2] * vec2[0])
vec[2] = vec1[0] * vec2[1] - vec1[1] * vec2[0]

print(f"Vektorski prozvod:\ni: {vec[0]}\nj: {vec[1]}\nk: {vec[2]}\n")