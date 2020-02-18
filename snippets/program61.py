#two subplots stacked vertically by default
fig,axs=plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x,y)
axs[1].plot(x,-y)
