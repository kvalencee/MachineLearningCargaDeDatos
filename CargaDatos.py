import traceback

def cargarDatos(ruta,delimitador):

    matriz=[]

    try:
        with open(ruta,'r') as base:
            for linea in base:
                lineaLimpia=linea.strip()
                if lineaLimpia!="":
                    atributos = lineaLimpia.split(delimitador)
                    matriz.append(atributos)
        return matriz


    except FileNotFoundError:
        return 0



def main():

    print("Ingresa el nombre del archivo")
    ruta = input()
    print("Ingresa el delimitador del archivo")
    delimitador = input()

    matriz=cargarDatos(ruta,delimitador)
    if matriz:
        patrones = len(matriz)
        atributos = len(matriz[0])

        print(f"El numero de patrones es: {patrones}")
        print(f"El numero de atributos es: {atributos}")
        # print("El contenido de la matriz es:")
        # for i in range(patrones):
        #     print(matriz[i])

        print("Especifica la columna CLASE: ")
        clase = int(input())


        # print(type(matriz))

        print(matriz[1][clase])

        # print("Columna clase de todos los atributos: ")
        # for i in range(atributos):
        #     print(f"{i}. {matriz[i[clase]]} ")

    else:
        print(f"El archivo no se encuentra")









main()



