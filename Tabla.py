numero=input("Dame un numero del 1 al 9:")
numero=int(numero)
for i in range(1,11):
    salida="{} X {} = {}"
    print(salida.format(numero,i,i*numero))