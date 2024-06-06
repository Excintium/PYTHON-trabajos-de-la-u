#crud
usuarios=[
    {"id_usuario":1,
    "nombre":"juan",
    "edad":20},
    {"id_usuario":2,
    "nombre":"pedro",
    "edad":30}
]

#crear
id_usuario=1
nombre=input("Ingrese un nombre: ")
edad=input("Ingrese una edad: ")
usuarios.append({"nombre":nombre,"edad":edad})

nombre=input("Ingrese un nombre: ")
edad=input("Ingrese una edad: ")
usuarios.append({"nombre":nombre,"edad":edad})

#leer
print("usuarios totales")
for usuario in usuarios:
    print(usuario)

#actualizar
posicion_usuario=0
nuevo_nombre=input("Ingrese el nuevo nombre: ")
nueva_edad=input("Ingrese la nueva edad: ")
usuario[id_usuario]["nombre"]=nuevo_nombre
usuario[id_usuario]["edad"]=nueva_edad

print("usuarios despues de actualizar")
for usuario in usuarios:
    print(usuario)

#eliminar por posicion (usando pop)
usuarios.pop(0)
print("usuarios despues de eliminar")
for usuario in usuarios:
    print(usuario)

#eliminar por valor (usando remove)
usuarios.remove({"nombre":"juan","edad":"20"})
print("usuarios despues de eliminar")
for usuario in usuarios:
    print(usuario)