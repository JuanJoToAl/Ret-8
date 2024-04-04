# Importamos módulo math (funciones matemáticas)
import math

# Variable: suma de la serie de Taylor
suma_aprox: float = 0
    
# Solicitud: valor de la variable
variable = float(input("Ingrese valor variable para evaluar seno: "))

# Solicitud: número del término
termino = int(input("Ingrese el número del término: "))

# Función seno evaluada en la variable
resultado = math.sin(float(variable))

# Bucle: cálculo de la suma de la serie de Taylor
for i in range(termino + 1):
    suma_aprox += (-1) ** i * (variable ** (2 * i + 1)) / math.factorial(2 * i + 1)

# Diferencia entre valor real y aproximación
diferencia_x = resultado - suma_aprox

# Error porcentual relativo
error = abs(diferencia_x / resultado) * 100

# Impresión: valor aproximado
print(f"Valor aprox. función en término ({termino}): {suma_aprox}")

# Impresión: valor real
print(f"Valor real función: {resultado}")

# Impresión: diferencia absoluta
print(f"Diferencia absoluta entre valor real y aprox.: {abs(diferencia_x)}")

# Bucle: iteración hasta error < 0.1%
while error >= 0.1:
    termino += 1
    suma_aprox += (-1) ** termino * (variable ** (2 * termino + 1)) / math.factorial(2 * termino + 1)
    diferencia_x = resultado - suma_aprox
    error = abs(diferencia_x / resultado) * 100

# Impresión: términos para error < 0.1%
print(f"Se obtiene menos del 0.1% error con {termino} términos.")