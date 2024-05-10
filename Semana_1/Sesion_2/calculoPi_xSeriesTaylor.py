import math
conta = 0
acumula = 0.0

division_actual = 1.0
essuma= True
while division_actual > 0.00052:
    conta += 1
    division_actual = 1/conta
    if conta %2!=0:
        if essuma:
            acumula +=1 /conta
        else:
            acumula -= division_actual
        essuma= not essuma

print("El cuarto del are es: ", acumula)
pi=acumula*4
print("Pi es igual a: ",pi)