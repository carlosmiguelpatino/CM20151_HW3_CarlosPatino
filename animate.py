import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation




col1 = []
col2 = [] 

for filename in os.listdir("./Test"):
	
	path  = "./Test/" + filename
	data = np.loadtxt(path)


	col1tmp = data[:,0]
	col2tmp = data[:,1]
        

        for i in range(len(col1tmp)):
                
                col1.append(float(col1tmp[i]))
                col2.append(float(col2tmp[i]))



fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
        x = col1[i]
        y = col2[i]
        ax1.clear()
        ax1.scatter(x,y)

anim = animation.FuncAnimation(fig, animate, interval=50, blit = True)

plt.show()

	

