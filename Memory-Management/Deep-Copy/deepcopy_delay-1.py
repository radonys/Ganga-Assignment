import copy
import time
from memory_profiler import profile
import sys

@profile
def deepcopy(i,simple_object):

	simple_object.append(copy.deepcopy(simple_object[i-1]))

	return simple_object

n = 5
simple_object = [[1,2,[3,4],5]]

for j in range(100000):
	simple_object[0].append([6])

for i in range(1,n):

	deepcopy(i,simple_object)
	time.sleep(5)

