# SENSACION TERMICA (WIND CHILL EFFECT)
# Calcula el indice de sensacion termica por frio a 0 ºC o bajo 0

WC_OFFSET = 13.112                                                              # Coeficientes determinados experimentalmente
WC_FACTOR1 = 0.6215
WC_FACTOR2 = -11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

temp = float(input("Temperatura (ºC): "))
speed = float(input("Velocidad del viento (km/h): "))       

wci = WC_OFFSET + \
      WC_FACTOR1 * temp + \
      WC_FACTOR2 * speed ** WC_EXPONENT + \
      WC_FACTOR3 * temp * speed ** WC_EXPONENT
      
print("El indice de sensacion termica es", round(wci))
