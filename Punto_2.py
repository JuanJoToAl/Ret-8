# Se determina el rango de números y el incremento
for i in range(1, 999+1, 1):
    
    # Si el número i modulo 2 igual a uno, se imprime el número i y el siguiente, 
    # el cuál debe ser par
    if i % 2 == 1:
        print("{:<10} {:<10}".format(i, i+1))  