# Se declara la variable 
cuadrado : int

# Se determina el rango de números y se calcula su cuadrado
for i in range(1, 100 + 1, 1):
    cuadrado= i ** 2

    # Se imprime el número i junto con su cuadrado
    print("El cuadrado de " + str(i) + " es " + str(cuadrado))