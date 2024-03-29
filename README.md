# Reto 8

_En el siguiente repositorio se exponen las soluciones a los puntos del reto 8_

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
# Se declara la variable 
cuadrado : int

# Se determina el rango de números y se calcula su cuadrado
for i in range(1, 100 + 1, 1):
    cuadrado= i ** 2

    # Se imprime el número i junto con su cuadrado
    print("El cuadrado de " + str(i) + " es " + str(cuadrado))
```

### 2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
# Se determina el rango de números y el incremento
for i in range(1, 999+1, 1):
    
    # Si el número i modulo 2 igual a uno, se imprime el número i y el siguiente, 
    # el cuál debe ser par
    if i % 2 == 1:
        print("{:<10} {:<10}".format(i, i+1))  
```

### 3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

```python
# Se declara variable
numero : int 
numero = int(input("Ingrese un número"))

# Se define que no hay pares naturales menores que 2
if numero < 2:
        print("El número es menor que 2")

# Se determina el rango de números y el decrecimiento    
else:
    for i in range(numero, 1, -1):
    
    # Si número módulo 2 es 0, el número es par, 
    # luego se resta 2 para seguir el otro par menor que número
        if i % 2 == 0:
            print(i) 
```  

### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

```python
# Se declaran variables e inicializa variable factor y producto
factor : int = 1
producto : int = 1
numero = int(input("Ingrese un número"))

if numero >= 0:

    # Se determina el rango de números y el dincremento  
    for i in range(1, numero+1, 1):

        # Se calcula e imprime el facotrial con su número
        producto *= factor
        factor += 1
        print("El factorial de " + str(i) + " es " +str(producto))

# Si se ingresa un número negativo, se imprime mensaje
else:
    print("Los número negativos no tienen factorial")
```

### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
# Se establecen las variables a ingresar por el usuario
exponente = int(input("Ingrese el valor de la potencia"))

# Se declara e inicializa la variable base
base : int = [2]

# Se establece el ciclo for para calcular la potencia
for i in base:
    potencia = i**exponente
    print(f" La potencia de 2 elevado a {exponente} es {potencia}")
```

### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. **Disclaimer:** Trate de no utilizar el operador de potencia (**).

```python
# Se establecen las variables a ingresar por el usuario
base = float(input("Ingrese el valor de la base"))
exponente = int(input("Ingrese el valor del exponente"))

# Se declara e inicializa la variable potencia
potencia : int = 1

# Se establece el ciclo for para calcular el valor de la potencia 
for i in range(exponente):
    potencia *= base
print(f" La potencia de {base} elevado a {exponente} es {potencia}")
```

### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```python
# Se establece el rango de las tablas de multiplicar a mostrar
for i in range(1, 10, 1):
    print(f"Tabla de multiplicar del {i}")

    #Se establece el rango de números que hacen parte de las tablas de multiplicar
    for b in range(1, 10, 1):
        c = i * b
        print(f"{i} x {b} = {c}")
```

### 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

**Disclaimer:** Para la aproximación de serie determine con que valor n se obtiene menos del 0.1% de error.

```python
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
```

### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

**Disclaimer:** Para la aproximación de serie determine con que valor n se obtiene menos del 0.1% de error.

```python
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
```

### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

**Disclaimer:** Para la aproximación de serie determine con que valor n se obtiene menos del 0.1% de error.

```python
# Importa módulo math (funciones matemáticas)
import math

# Solicitud: valor de la variable
variable = float(input("Ingrese valor variable en el rango [-1, 1]: "))

# Solicitud: número del término
termino = int(input("Ingrese el número del término: "))

# Valida rango de la variable
if -1 <= variable <= 1:
    
    # Variable: suma de la serie de Taylor
    sumatoria_aprox: float = 0
    
    # Función atan evaluada en la variable
    resultado = math.atan(float(variable))

    # Bucle: cálculo de la suma de la serie de Taylor
    for i in range(termino + 1):
        sumatoria_aprox += ((-1)**i) * (variable**(2 * i + 1)) / (2 * i + 1)

    # Diferencia entre valor real y aproximación
    diferencia_x = resultado - sumatoria_aprox

    # Error porcentual relativo
    error = abs(diferencia_x / resultado) * 100

    # Impresión: valor aproximado
    print(f"Valor aprox. función ({termino}): {sumatoria_aprox}")

    # Impresión: valor real
    print(f"Valor real función: {resultado}")

    # Impresión: diferencia absoluta
    print(f"Diferencia absoluta entre valor real y aprox.: {abs(diferencia_x)}")

    # Bucle: iteración hasta error < 0.1%
    while error >= 0.1:
        termino += 1
        sumatoria_aprox += ((-1)**termino) * (variable**(2 * termino + 1)) / (2 * termino + 1)
        diferencia_x = resultado - sumatoria_aprox
        error = abs(diferencia_x / resultado) * 100

    # Impresión: términos para error < 0.1%
    print(f"Se obtiene menos del 0.1% error con {termino} términos.")
    
else:
    # Imprime mensaje de error si no está en el rango
    print("El valor de la variable no está en el rango [-1, 1]")
```
