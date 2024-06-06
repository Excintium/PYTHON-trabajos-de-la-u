import os
#arreglo [3][4]
matriz=[
    [],
    [],
    []
]

#primera fila
while True:
    for i in range(4):
        print(" números para ingresar en la primer fila (3,10,4,16)")
        numeros_fila_1=int(input(""))
        matriz[0].append(numeros_fila_1)
        os.system("cls")
    for i in range(4):
        print("numeros para la fila 2 ( 1,7,8,-7)")
        numeros_fila_2=int(input(""))
        matriz[1].append(numeros_fila_2)
        os.system("cls")
    for i in range(4):
        print("numeros para la fila 3 (9,-1,3,9)")
        numeros_fila_3=int(input(""))
        matriz[2].append(numeros_fila_3)
        os.system("cls")
    break
for i in matriz:
    print(i)

#arreglo[3][3][3]
