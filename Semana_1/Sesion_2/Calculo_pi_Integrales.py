import math
divisiones = 10000

cuarto_area = 0.0
acumula = 0
for i in range(divisiones):
    acumula += 1
    baseT = float(acumula)/float(divisiones)
    altura = math.sqrt(1-baseT*baseT) 
    base = 1/float(divisiones)
    cuarto_area += base*altura

print("El cuarto del are es: ", cuarto_area)
pi=cuarto_area*4
print("Pi es igual a: ",pi)