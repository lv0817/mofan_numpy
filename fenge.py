import numpy as np 

A = np.arange(12).reshape(3,4)
print(A)

print(np.split(A,[1,1,2],axis=1))