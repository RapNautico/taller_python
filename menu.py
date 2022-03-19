from operator import index

# productos = []
codigos = ['001', '002']
nombres = ['pera', 'uva']
precios = [2000, 3000]

# print("Compras El MochoCaido")
# print("**********************************************")
# print("0. Salir")
# print("1. Digitar 1 para ingresar {código, nombre, precio} de un producto")
# print("2. Digitar 2 para mostrar todos los productos registrados")
# print("3. Digitar 3 para permitir buscar por código un producto y editar el precio de este")
# print("4. Digitar 4 para permitir buscar por código un producto y eliminar el producto")
# print("**********************************************")

opcion = int(input("\n Comparas el MochoCaido \n \n 0. Salir \n 1. Digitar 1 para ingresar {código, nombre, precio} de un producto \n 2. Digitar 2 para mostrar todos los productos registrados \n 3. Digitar 3 para permitir buscar por código un producto y editar el precio de este \n 4. Digitar 4 para permitir buscar por código un producto y eliminar el producto \n \n Digita una opcion: "))
print("-------------------------")

while(opcion != 0):
    # opcion = int(input("Digita una opcion: "))
    # producto = {
    #     }
    #pregunte por la opcion
    if(opcion == 0):
        break
    elif(opcion == 1):
        print("Llena los siguientes datos del producto... ")
        print("-------------------------")
        codigos.append(input("Escriba el codigo del producto: "))
        nombres.append(input("Escriba el nombre del producto: ")) 
        precios.append(int(input("Escriba el precio del producto: ")))
        print("-------------------------")
        input("Presione enter para continuar >> ")
        print("-------------------------")
    elif(opcion == 2):
        print("Codigo |  Nombre       |  Precio    |")
        for i in range(len(codigos)):
            print(codigos[i],"       ", nombres[i],"           ",precios[i])
        print("-------------------------")
        input("Presione enter para continuar >> ")
        print("-------------------------")
    elif(opcion == 3):
        codigo = input("ingrese el codigo del producto para poder editarlo: ")
        print("-------------------------")
        for i in range(len(codigos)):
            if codigos[i] == codigo:
                precios[i] = input("Cual es el nuevo precio del producto: ")
        print("-------------------------")
        print(f"el precio del producto se a actualizado, por favor verifiquelo en la lista") 
        print("-------------------------")
        input("Presione enter para continuar >> ")
        print("-------------------------")
    elif(opcion == 4):
        codigo = input("ingrese el codigo del producto para poder eliminarlo: ")
        print("-------------------------")
        for i in range(len(codigos)-1,-1,-1):
            if codigos[i] == codigo:
                codigos.pop()
                nombres.pop()
                precios.pop()
        print("El producto se ha eliminado correctamente")
        print("-------------------------")
        input("Presione enter para continuar >> ")
        print("-------------------------")
    else:
        print("El numero no es valido")
    opcion = int(input("Comparas el MochoCaido \n \n 0. Salir \n 1. Digitar 1 para ingresar {código, nombre, precio} de un producto \n 2. Digitar 2 para mostrar todos los productos registrados \n 3. Digitar 3 para permitir buscar por código un producto y editar el precio de este \n 4. Digitar 4 para permitir buscar por código un producto y eliminar el producto \n \n Digita una opcion: "))
    print("-------------------------")