import sys

def joinbruto(archivo):
    joinfinal = ""
    conjunto1 = {}
    conjunto2 = {}

    nelems1 = int(archivo.readline(1))
    archivo.readline() #skip linea
    columnas1 = archivo.readline().strip().split()
    tuplas1 = int(archivo.readline(1))
    archivo.readline() #skip linea
    parametros1 = []
    cont = 0
    while cont != nelems1:
        conjunto1[columnas1[cont]] = []
        cont += 1

    i = 0
    while i != tuplas1:
        parametros1 = archivo.readline().strip().split()
        cont = 0
        while cont != nelems1:
            conjunto1[columnas1[cont]].append([parametros1[cont], tuple(parametros1)])
            cont += 1   
        i += 1

    nelems2 = int(archivo.readline(1))
    archivo.readline() #skip linea
    columnas2 = archivo.readline().strip().split()
    tuplas2 = int(archivo.readline(1))
    archivo.readline() #skip linea
    parametros2 = []
    cont = 0
    while cont != nelems2:
        conjunto2[columnas2[cont]] = []
        cont += 1

    i = 0
    while i != tuplas2:
        parametros2 = archivo.readline().strip().split()
        cont = 0
        while cont != nelems2:
            conjunto2[columnas2[cont]].append([parametros2[cont], tuple(parametros2)])
            cont += 1   
        i += 1

    # una vez guardados los datos desde el archivo, recorremos los diccionarios
    # en busca de coincidencias para hacer el join

    check = 0
    for i in conjunto1:
        for j in conjunto2:
            if i == j:
                check = 1

    if not check:
        print("no hay coincidencias.")
        
    else:
        colmatch = []
        columnas = ()
        numcolumnas = 0
        numfilas = 0
        for j in conjunto2:
            datos2 = conjunto2[j]
            for i in conjunto1:
                datos1 = conjunto1[i]
                if i not in columnas:
                    columnas += (i,)
                    numcolumnas += 1
                for x, tupla1 in datos1:
                    for y, tupla2 in datos2:
                        if x == y and i == j:
                            colmatch.append([tupla1, tupla2])
                            numfilas += 1
            if j not in columnas:
                    columnas += (j,)
                    numcolumnas += 1
                    
        joinfinal += str(numcolumnas) + "\n"
        respuesta = ""
        for n in columnas:
            respuesta += n + " "
        joinfinal += respuesta + "\n"
        joinfinal += str(numfilas) + "\n"
        
        for listamatch in colmatch:
            tupla1, tupla2 = listamatch
            final = tupla1
            ocurrencia = 1
            for n in tupla2:
                if n in final and ocurrencia == 1:
                    ocurrencia = 0
                    continue
                else:
                    final += (n,)  
            text = ""
            for n in final:
                text += n + " "
            joinfinal += text + "\n"
    return joinfinal

file1 = sys.argv[1]
archivo1 = open(file1, "r")

respuesta1 = joinbruto(archivo1)
print("RESPUESTA 1:\n")
print(respuesta1)

archivo1.close()

#######################
# Grafos
#######################
file2 = sys.argv[2]
archivo2 = open(file2, "r")

nelems = "2"
tuplas = 0
for linea in archivo2:
    tuplas += 1

archivo2.close()

archivo2 = open(file2, "r")
formato = open("formato.txt", "w")

formato.write(nelems + "\n")
formato.write("0 1\n")
formato.write(str(tuplas) + "\n")

for linea in archivo2:
    formato.write(linea)

formato.write("\n")
archivo2.close()

archivo2 = open(file2, "r")
formato.write(nelems + "\n")
formato.write("1 2\n")
formato.write(str(tuplas) + "\n")

for linea in archivo2:
    formato.write(linea)


formato = open("formato.txt", "r")
primerjoin = joinbruto(formato)

respuestas = primerjoin.split("\n")
triangulos = int(respuestas[2])//3
print("RESPUESTA 2:\n")
print("La cantidad de trinagulos es:", triangulos, "\n")
