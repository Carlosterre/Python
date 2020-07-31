# CAIDA LIBRE
# Calcula la velocidad que tiene un objeto al tocar el suelo tras ser soltado desde una altura

from math import sqrt

GRAVITY = 9.8                                                                  # m/(s^2)

d = float(input("Altura a la que se suelta el objeto (m): "))

vf = sqrt(2 * GRAVITY * d)

print("Llegara al suelo a", vf, "m/s")
