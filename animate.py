import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("Graficas")

for filename in os.listdir("./Test"):
	
	path  = "./Test/" + filename
	data = np.loadtxt(path)

	col1 = data[:,0]
	col2 = data[:,1]

	plt.plot(col1, col2)
	plt.title(filename)
	imagepath = filename[:-4]
	imagepath = "./Graficas/"+ imagepath + ".png"
	plt.savefig(imagepath)




	

