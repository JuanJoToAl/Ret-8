# Se establece el rango de las tablas de multiplicar a mostrar
for i in range(1, 10, 1):
    print(f"Tabla de multiplicar del {i}")

    #Se establece el rango de números que hacen parte de las tablas de multiplicar
    for b in range(1, 10, 1):
        c = i * b
        print(f"{i} x {b} = {c}")