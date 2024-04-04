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
   
     