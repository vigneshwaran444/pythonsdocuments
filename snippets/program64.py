import numpy as np
import pandas as pd
import matplotlib.pylot as plt
from sklearn.linear_model import LinearRegression
x=np.arange(0,100)
y=np.arange(0,100)
print(x)
print(y)
lr=LinearRegression()

x.ndim
y.ndim

x.shape
y.shape

x=x.reshape(-1,1)
x.shape(-1,1)

x.ndim

lr.fit(x,y)

plt.scatter(x,y,color='red')

plt.plot(x,lr.prdict(x),color='blue')
plt.title('Linear Regression Demo')
plt.xlabel('X')
plt.ylabel('y')


plt.show()
