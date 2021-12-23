from sys import *

def BBinaria2(listaLibros, posPrimero, posUltimo, dinero):

    sumaTotal = listaLibros[posPrimero] + listaLibros[posUltimo]

    if sumaTotal == dinero:

        return (posPrimero, posUltimo)

    elif sumaTotal > dinero:

        return BBinaria2(listaLibros, posPrimero, posUltimo - 1, dinero)

    else:

        return BBinaria2(listaLibros, posPrimero + 1, posUltimo, dinero)


tamArray = int(stdin.readline().strip())

listaLibros = []

lineaPrecios = stdin.readline().strip().split()
for precio in lineaPrecios:
    listaLibros.append(int(precio))

presupuesto = int(stdin.readline().strip())


resultado = BBinaria2(listaLibros, 0, len(listaLibros)-1, presupuesto)
i, j = resultado

pos1 = str(i + 1)
pos2 = str(j + 1)

stdout.write(pos1+" "+pos2+"\n")