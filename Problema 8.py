def Sacareltiempo (Distancia, Velocidad):
    TiempoEstimado = Distancia / Velocidad
    return TiempoEstimado

DistanciaEstimada = int(input("Por favor de ingresar la Distancia \n"))
VelocidadEstimada = int(input("Por favor de ingresar la Velocidad \n"))
TiempoEstimado = Sacareltiempo (DistanciaEstimada, VelocidadEstimada)
print("El tiempo es de: {}" .format(TiempoEstimado))
