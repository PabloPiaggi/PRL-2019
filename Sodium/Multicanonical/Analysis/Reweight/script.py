import numpy as np

temp=np.arange(400,605,5)

print("# vim:ft=plumed")
print("")
print("energy: READ FILE=../COLVARtrim VALUES=energy  IGNORE_TIME")
print("b1: READ FILE=../COLVARtrim VALUES=b1.bias  IGNORE_TIME")
print("")
print("energyshift: COMBINE ARG=energy PARAMETERS=-24300 PERIODIC=NO")
print("weights: REWEIGHT_BIAS TEMP=500 ARG=b1.bias")

print("")

print("PRINT ARG=* FILE=COLVAR STRIDE=1 FMT=%16.10f")

print("")

for i in range(temp.shape[0]):
	name=str(int(temp[i]))
	print("weights" + name  + ": REWEIGHT_TEMP_PRESS TEMP=500 REWEIGHT_TEMP=" + str(temp[i]) + " ENERGY=energyshift")
	print("avg-" + name + ": AVERAGE ARG=energy LOGWEIGHTS=weights,weights" + name + " CLEAR=2000")
	print("PRINT ARG=avg-" + name + ",weights,weights" + name + " FILE=COLVAR" + name + " STRIDE=2000 FMT=%16.10f")
	print("")
