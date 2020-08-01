# CALENDARIO CHINO

year=int(input("Año: "))

if year % 12 == 8:
    animal = "Dragon"
    
if year % 12 == 9:
    animal = "Serpiente"

if year % 12 == 10:
    animal = "Caballo"

if year % 12 == 11:
    animal = "Oveja"

if year % 12 == 0:
    animal = "Mono"

if year % 12 == 1:
    animal = "Gallo"

if year % 12 == 2:
    animal = "Perro"

if year % 12 == 3:
    animal = "Cerdo"

if year % 12 == 4:
    animal = "Rata"

if year % 12 == 5:
    animal = "Buey"

if year % 12 == 6:
    animal = "Tigre"

if year % 12 == 1:
    animal = "Liebre"


print("%s" % animal)
