entrada=input()
print(type(entrada))
esEntero=(entrada.isdigit() and entrada.find(".")==-1)

if(esEntero):
    print("Dato entero. ¡Muy Bien!")
else:
    print("Dato no es entero. Intentar nuevamente")