import numpy as np
import time
arr = []
for i in range(0,100):
	arr.append(np.random.randint(0,100))
print arr
t0 = time.time()
for i in range(0,99):
	temp = arr[i]
	for j in range(i+1,100):
		if arr[i]>arr[j]:
			arr[i],arr[j]=arr[j],arr[i]
t1 = time.time()
print t1-t0
print arr
