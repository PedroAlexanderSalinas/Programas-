Cuantas = int(input("Dame la cantidad de nombres que deseas guardar \n"))
Contador = 1
NombresGuardados = []

while Contador <= Cuantas:
    Nombre = input("Dame el nombre que quieras que guarde \n")
    Contador = Contador + 1
    NombresGuardados = NombresGuardados + [Nombre]
print (NombresGuardados) 
