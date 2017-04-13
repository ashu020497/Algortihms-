import time
import numpy as np
arr = []
for i in range(0,100):
	arr.append(np.random.randint(0,100))
print arr
t0 = time.time()
for j in range(0,100):
	for i in range(0,99):
		if arr[i]>arr[i+1]:
			arr[i],arr[i+1]=arr[i+1],arr[i]
t1 = time.time()
print t1-t0
print arr
