import numpy as np
from scipy.signal import convolve2d
A=np.array([[1,0,0,1,0],[0,1,1,0,1],[1,0,1,0,1],[1,0,0,1,0],[0,1,1,0,1]])
B=np.array([[1,0,1],[1,1,0],[0,0,1]])
C=convolve2d(A,B,'valid')

print(c)
[[5 1 3]]
[[2 3 2]]
[[2 2 4]]
