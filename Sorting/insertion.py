import numpy as np
import time
arr = []
for in range(0,100):
	arr.append(np.random.randint(0,100))
t0 = time.time()
for i in range(1,100):
	for j in range(0,j):
		if arr[i]<arr[j]:
			arr[i],arr[j]=arr[j],arr[i]
t1 = time.time()
print t1-t0
