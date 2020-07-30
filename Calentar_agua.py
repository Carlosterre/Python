# CALENTAR AGUA
# Cantidad de energia necesaria para calentar un volumen de agua

ELECTRICITY_PRICE = 0.192699                                                   # Tarifa General 2.0A (19:00 a 20:00) en 2020

WATER_HEAT_CAPACITY = 4184                                                     # J (1 cal)
J_TO_KWH = 2.77778e-7

volume = float(input("Litros de agua: "))
d_temp = float(input("Incremento de temperatura (ºC): "))

q = volume * d_temp * WATER_HEAT_CAPACITY

print("Se necesitan", q, "J")

kwh = q * J_TO_KWH

cost = kwh * ELECTRICITY_PRICE

print("Cuesta", cost, "€")
