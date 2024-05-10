import random
import math
cuantos = 10000
cuantossi=0

for i in range(cuantos):
    x = random.random()
    y = random.random()

    y_calculada = math.sqrt(1-x*x)
    if y >y_calculada:
        None
    else:
        cuantossi += 1

cuarto_de_area= float(cuantossi)/ float(cuantos)
pi = cuarto_de_area*4
print("El cuarto de pi es: ", cuarto_de_area)
print("Pi: ", pi)