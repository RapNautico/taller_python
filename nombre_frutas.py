#-Leer el nombre de 10 frutas para preparar un salpicón; el programa debe
#permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido
#inverso al ingresado+(1)

frutas = []

#Esculcando en la lista
for fruta in range(10):
    ingreseFruta = input("ingrese una fruta: ")
    frutas.append(ingreseFruta)
print("------------------------")
for i in reversed(frutas):
    print(i)
    