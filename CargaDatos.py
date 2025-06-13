def cargarDatos(ruta,delimitador):
    numAtributos=0
    numPatrones=0
    try:
        with open(ruta,'r') as base:
            for linea in base:
                lineaLimpia=linea.strip()
                if lineaLimpia!="":
                    atributos = lineaLimpia.split(delimitador)
                    print(atributos)
                    numPatrones = numPatrones + 1

        print(f"El numero de patrones es {numPatrones}")
        print(f"El numero de atributos es {numAtributos}")
    except FileNotFoundError:
        print("No se encuentra el archivo")



def main():
    print("Ingresa el nombre del archivo")
    ruta = input()
    print("Ingresa el delimitador del archivo")
    delimitador = input()
    cargarDatos(ruta,delimitador)


main()



