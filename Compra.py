numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numero proporciondados: {} y {}. {}."
if (numero1==numero2):
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    if numero1>numero2:
        print(salida.format(numero1, numero2, "El mayor es el primero"))
    else:
        print(salida.format(numero1, numero2, "El mayor es el segundo"))