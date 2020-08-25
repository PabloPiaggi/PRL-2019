import numpy as np

temp=np.arange(400,605,5)

for i in range(temp.shape[0]):
	name="COLVAR" + str(int(temp[i]))
	data=np.genfromtxt(name)
	ene=data[1:,1]
	N=ene.shape[0]
	print(temp[i],np.mean(ene),np.std(ene),np.std(ene)/np.sqrt(N),np.amax(ene),np.amin(ene))
	
