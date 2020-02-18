#two subplots stacked in one row side by side
fig,(ax1,ax2)=plt.subplots(1,2)
fig.suptitle('horizontally stacked subplots')
ax1.plot(x,y)
ax2.plot(x,-y)

subplots(ROWCOUNT [COLUMNCOUNT])
