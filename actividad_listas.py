import os
#nombre mas largo
lista_nombre=[]
for i in range(3):
    nombre=input(f"Ingrese el nombre {i+1}: ")
    lista_nombre.append(nombre)
nombre_mas_largo= max(lista_nombre,key=len)
print(f"El nombre mas largo es: {nombre_mas_largo}")

#nombres y apellidos
nombres=[]
apellidos=[]

for i in range(3):
    agregar_nombre=input("Ingresa el nombre a agregar: ")
    nombres.append(agregar_nombre)

for i in range(3):
    agregar_apellido=input("Ingresa el apellido a agregar: ")
    apellidos.append(agregar_apellido)
print(nombres)
print(apellidos)

#almacenar nombres hasta que no quiera mas
nombre=[]
while True:
    print("Desea agregar un nombre a la lista? ")
    print("si/no")
    respuesta=input("Ingresa tu opción: ").lower()

    if respuesta == "si":
        agregar_nombre=input("ingresa el nombre a agregar")
        nombre.append(agregar_nombre)
    elif respuesta == "no":
        print("vamos a eliminar el nombre mas corto")
        nombre_mas_corto= min(nombre,key=len)
        print(f"el nombre mas corto es {nombre_mas_corto}")
        nombre.remove(nombre_mas_corto)
        break
print(nombre)

# menu para registrar usuarios
usuarios=[]
while True:
    print("1) iniciar sesión")
    print("2) Registrar usuario")
    print("3) Eliminar usuario")
    print("4) Salir")
    opcion=input("Ingresa tu opción: ")
    if opcion == "1":
        print("Ingrese nombre de usuario: ")
        usuario=input()
        print("Ingrese su clave: ")
        clave=input()
        if usuario in usuarios:
            print("Usuario encontrado")
        else:
            print("Usuario no encontrado")
    elif opcion == "2":
        print("Registrar usuario")
        nuevo_usuario=input("Ingrese un nombre de usuario: ")
        print("Ingrese su clave: ")
        nueva_clave=input()
        print("Reingrese su clave: ")
        nueva_clave2=input()
        usuarios.append(nuevo_usuario)
        if nueva_clave == nueva_clave2:
            print("Usuario registrado")
        else:
            print("Las claves no coinciden")
    elif opcion == "3":
        print("Eliminar usuario")
        print("Ingrese el nombre de usuario a eliminar: ")
        eliminar=input()
        print("Ingrese la clave para eliminar: ")
        clave_eliminar=input()
        print("Esta seguro que desea eliminar este usuario? si/no")
        respuesta=input()
        if respuesta == "si":
            print("Usuario eliminado")
            usuarios.remove(eliminar)
        else:
            print("Usuario no eliminado")
    elif opcion == "4":
        print("Salir")
        break

#ventas de supermercado
carro_de_compras=[]

while True:
    print("1) Agregar producto")
    print("2) Ver Canasta")
    print("3) Ver total")
    print("4) Salir")
    opcion=input("Ingresa tu opción: ")
    os.system("cls")
    if opcion == "1":
        os.system("cls")
        print("Productos Disponibles: ")
        print("1) Arroz $990")
        print("2) Fideos $1.100")
        print("3) Leche $750")
        print("4) Pan $1.000")
        print("5) Té $800")
        producto_a_agregar=input("Seleccione su producto: ")
        os.system("cls")
        if producto_a_agregar == "1":
            carro_de_compras.append("Arroz")
        elif producto_a_agregar == "2":
            carro_de_compras.append("Fideos")
        elif producto_a_agregar == "3":
            carro_de_compras.append("Leche")
        elif producto_a_agregar == "4":
            carro_de_compras.append("Pan")
        elif producto_a_agregar == "5":
            carro_de_compras.append("Té")
    elif opcion == "2":
        os.system("cls")
        print("\nCanasta de compras: ")
        for producto in carro_de_compras:
            print(producto)
    elif opcion == "3":
        os.system("cls")
        total =0
        for i in carro_de_compras:
            if i == "Arroz":
                total+=990
            elif i == "Fideos":
                total+=1100
            elif i == "Leche":
                total+=750
            elif i == "Pan":
                total+=1000
            elif i == "Té":
                total+=800
        print(f"El total de la compra es: ${total}")
    elif opcion == "4":
        os.system("cls")
        print("Gracias por preferirnos")
        break