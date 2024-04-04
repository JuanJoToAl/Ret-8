# Se establecen las variables a ingresar por el usuario
base = float(input("Ingrese el valor de la base"))
exponente = int(input("Ingrese el valor del exponente"))

# Se declara e inicializa la variable potencia
potencia : int = 1

# Se establece el ciclo for para calcular el valor de la potencia 
for i in range(exponente):
    potencia *= base
print(f" La potencia de {base} elevado a {exponente} es {potencia}")
