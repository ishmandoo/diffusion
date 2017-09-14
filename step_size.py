from particles import *

# changing step size
traps = []
parts = []
for i in range(100):
	if len(traps) > 0:
		left = traps[-1]
	else:
		left = None

	# lower visc right
	new_trap = Trap(float(i)**1.5, left, None, 0.25, 0.25)

	if len(traps) > 0:
		traps[-1].right = new_trap


	traps.append(new_trap)

	if 40 <= i <= 60:
		for i in range(1000):
			parts.append(Particle(new_trap))

for i in range(10):
	for part in parts:
		part.step()


print np.mean([part.getDisplacement() for part in parts])

'''
This seems to produce drift toward low viscosity
'''