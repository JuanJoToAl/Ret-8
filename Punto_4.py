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