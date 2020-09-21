"""
This doc is used to find the calculate the gravitational force between two masses!
Using formula : GMm/r**2 where G is the gravitational constant, M and m are the two masses, and r is
the distance between them.

G = 6.67 * 10-11
MEarth = 6.0 * 1024
mMoon = 7.34 * 1022
r = 3.84 * 108
"""

G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)
m = 7.34 * (10 ** 22)
r = 3.84 * (10 ** 8)

grav_force = (G * M * m)/(r**2)
print(grav_force)

