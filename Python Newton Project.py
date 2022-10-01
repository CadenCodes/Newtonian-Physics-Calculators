from operator import contains

print("Lets find the force of gravity between two objects using Newton's Laws!")

G = 6.67*10 ** -11
# Gravitation constant in Newton meters squared over kilograms squared
m1 = input("What is the mass of one of the bodys in the system in Kg?")
m2 = input("What is the mass of the second body in the system in Kg?")
r = input("What is the average distance between the two bodies in meters?")

if "e" in m1:
    fm1 = float(m1)
    im1 = int(fm1)
else:
    im1 = int(m1)
if "e" in m2:
    fm2 = float(m2)
    im2 = int(fm2)
else:
    im2 = int(m2)
if "e" in r:
    fr = float(r)
    ir = int(fr)
else:
    ir = int(r)

F = G * ((im1 * im2)/(ir ** 2))

print("Force is ",F," Newtons")
