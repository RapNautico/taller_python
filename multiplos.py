#-Construir un programa que permita ingresar N 
# (cantidad digitada por el usuario) números enteros 
# y cuente cuantos múltiplos de 2 y de 3 fueron ingresados (+1)

multiplos = 0

longitudLista = int(input("Ingrese el tamaño de la lista: "))
print(f"multiplos de 2 y de 3 entre 1 y %i: "%longitudLista)
for i in range(1,longitudLista+1):
    if i%2==0 and i%3==0:
        multiplos+=1
        print(i)
print(f"existen %i multiplos de 2 y 3 en ese rango, incluidos los extremos"%multiplos)