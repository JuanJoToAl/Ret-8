# Se establecen las variables a ingresar por el usuario
exponente = int(input("Ingrese el valor de la potencia"))

# Se declara e inicializa la variable base
base : int = [2]

# Se establece el ciclo for para calcular la potencia
for i in base:
    potencia = i**exponente
    print(f" La potencia de 2 elevado a {exponente} es {potencia}")
