from matplotlib.ticker import NullFormatter
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
y=np.random.normal(loc=0.5,scale=0.4,size=1000)
y=y[(y>0)&(y<1)]
y.sort()
x=np.arange(len(y))

#plot with various axes scales
plt.figure()

#linear
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


#log
plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


#symmetric log
plt.subplot(223)
plt.plot(x,y-y.mean())
plt.yscale('symlog',linthreshy=0.01)
plt.grid(True)


#logit
plt.subplot(224)
plt.plot(x,y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)


plt.subplots_adjust(top=0.92,bottom=0.08,left=0.10,right=0.95,hspace=0.25,wspace=0.35)

plt.show()
