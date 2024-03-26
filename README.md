# Ret-8
```python
import math
def diferencia(variable : float, termino : int) -> None:    
    
    sumatoria_aprox : float = 0
    resultado = math.sin(float(variable))

    for i in range(termino + 1):
        sumatoria_aprox +=  ((-1) ** i) * (variable ** (2 * i + 1)) / math.factorial(2 * i + 1)
    
    diferencia_x = resultado - sumatoria_aprox
    error = abs(diferencia_x / resultado) * 100

    print(f"Valor aproximado de la función en el término {termino} de la sumatoria: {sumatoria_aprox}")
    print(f"Valor real de la función: {resultado}")
    print(f"Diferencia absoluta entre el valor real de la función y la aproximación: {abs(diferencia_x)}")
    
    while error >= 0.1:
        termino += 1
        sumatoria_aprox +=  ((-1) ** termino) * (variable ** (2 * termino + 1)) / math.factorial(2 * termino + 1)
        diferencia_x = resultado - sumatoria_aprox
        error = abs(diferencia_x / resultado) * 100

    print(f"Se obtiene menos del 0.1% de error con {termino} términos.")

if __name__ == "__main__":
    variable = float(input("Ingrese el valor de variable para evaluar seno"))
    termino = int(input("Ingrese el número del término"))
    diferencia(variable, termino)
```

```python  
import math
def diferencia(exponente : float, termino : float) -> None:    
    
    sumatoria_aprox : float = 0

    resultado = math.exp(float(exponente))

    for i in range(termino + 1):
        sumatoria_aprox += exponente**i/math.factorial(i)

    diferencia_x = resultado - sumatoria_aprox
    error = abs(diferencia_x / resultado) * 100 

    print(f"Valor aproximado de la función en el término {termino} de la sumatoria: {sumatoria_aprox}")
    print(f"Valor real de la función: {resultado}")
    print(f"Diferencia absoluta entre el valor real de la función y la aproximación: {abs(diferencia_x)}")

    while error >= 0.1:
        termino += 1
        sumatoria_aprox +=  exponente**termino/math.factorial(termino)
        diferencia_x = resultado - sumatoria_aprox
        error = abs(diferencia_x / resultado) * 100
    
    print(f"Se obtiene menos del 0.1% de error con {termino} términos.")

if __name__ == "__main__":
    exponente = float(input("Ingrese el valor del exponente de e"))
    termino = int(input("Ingrese el número del término"))
    diferencia(exponente, termino)
```

    

```python
import math

def condicion(variable : float, termino : int) -> None:

    if -1 <= variable and variable <= 1:
        diferencia(variable, termino)
    else:
        print("El valor de la variable no está en el rango determinado")

def diferencia(variable : float, termino : int) -> None:

    sumatoria_aprox : float = 0
    resultado = math.atan(float(variable))
    for i in range(termino + 1):
        sumatoria_aprox += ((-1)**i)* (variable**(2 * i + 1) /(2 * i + 1))
    diferencia_x = resultado - sumatoria_aprox
    error = abs(diferencia_x / resultado) * 100

    print(f"Valor aproximado de la función en el término {termino} de la sumatoria: {sumatoria_aprox}")
    print(f"Valor real de la función: {resultado}")
    print(f"Diferencia absoluta entre el valor real de la función y la aproximación: {abs(diferencia_x)}")
    
    while error >= 0.1:
        termino += 1
        sumatoria_aprox += ((-1)**termino)* (variable**(2 * termino + 1) /(2 * termino + 1))
        diferencia_x = resultado - sumatoria_aprox
        error = abs(diferencia_x / resultado) * 100

    print(f"Se obtiene menos del 0.1% de error con {termino} términos.")
    
    
if __name__ == "__main__":
    variable = float(input("Ingrese el valor de la variable entre -1 y 1 incluyendo a estos dos"))
    termino = int(input("Ingrese el número del término"))
    condicion(variable, termino)
```

