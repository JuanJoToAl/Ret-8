# Importamos módulo math (funciones matemáticas)
import math

# Se crea variable para almacenar suma de la serie de Taylor
sumatoria_aprox: float = 0

# Solicitud: valor del exponente
exponente = float(input("Ingrese el valor del exponente de e: "))

# Solicitud: número del término
termino = int(input("Ingrese el número del término: "))

# Función exponencial evaluada en el exponente
resultado = math.exp(float(exponente))

# Bucle: cálculo de la suma de la serie de Taylor
for i in range(termino + 1):
    sumatoria_aprox += exponente**i / math.factorial(i)

# Diferencia entre valor real y aproximación
diferencia_x = resultado - sumatoria_aprox

# Se calcula el error porcentual relativo
error = abs(diferencia_x / resultado) * 100

# Impresión: valor aproximado
print(f"Valor aprox. función en término ({termino}): {sumatoria_aprox}")

# Impresión: valor real
print(f"Valor real función: {resultado}")

# Impresión: diferencia absoluta
print(f"Diferencia absoluta entre valor real y aprox.: {abs(diferencia_x)}")

# Bucle: iteración hasta error < 0.1%
while error >= 0.1:
    termino += 1
    sumatoria_aprox += exponente**termino / math.factorial(termino)
    diferencia_x = resultado - sumatoria_aprox
    error = abs(diferencia_x / resultado) * 100

# Impresión: términos para error < 0.1%
print(f"Se obtiene menos del 0.1% error con {termino} términos.")