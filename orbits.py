# PROBLEMS:
# 	- At small dt (<0.2 s), the orbit diagram is a straight line that slowly falls off
#	- At large dt (>0.2 s), the orbit decays

import numpy as np

# Output file
out = open("out.csv", "w")

# Object array
objects = ["Earth", "ISS"]

# Mass array [kg]
m = [5.972E+24, 100E+3]

# Position array (x, y, z) [m]
p = np.array([[0, 0, 0], [6786.1E+3, 0, 0]])

# Velocity array (u, v, w) [m/s]
v = np.array([[0, 0, 0], [0, 7600, 0]])

# Acceleration array (a, b, c) [m/s^2]
a = np.array([[0.0, 0, 0], [0.0, 0.0, 0.0]])

dt = 0.02				# [s]
G = 6.674E-11			# [m^3 kg^-1 s^-2]

# Simulation parameters
timeMax = 3600 			# [s]
writeInterval = 20		# [s]

nt = int(timeMax / dt + 1)

for n in range(1, nt):
	t = n * dt

	# Run numbers for Shuttle:
	r = p[0] - p[1]									# Displacement vector from shuttle to Earth
	rNorm = np.linalg.norm(r)

	a[1] = (G * m[0] / rNorm**2) * (r / rNorm)		# Magnitude * direction unit vector
	p[1] = (0.5 * a[1] * dt**2) + (v[1] * dt) + p[1]
	v[1] = (a[1] * dt) + v[1]

	# v[1] = np.add(v[1], 	  a[1] * dt, 				out = v[1], casting = "unsafe")
	# p[1] = np.add(p[1], 0.5 * a[1] * dt**2 + v[1] * dt, out = p[1], casting = "unsafe")

	if t % writeInterval == 0:
		print("Step {}: t = {} s".format(n, t))
		print("x, y, z = {}, {}, {}".format(p[1][0], p[1][1], p[1][2]))
		print("u, v, w = {}, {}, {}".format(v[1][0], v[1][1], v[1][2]))
		print("a, b, c = {}, {}, {}".format(a[1][0], a[1][1], a[1][2]))
		print()
		out.write("{}, {}, {}, {}\n".format(t, p[1][0], p[1][1], p[1][2]))