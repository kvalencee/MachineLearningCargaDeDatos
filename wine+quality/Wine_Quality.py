#Nombre: Quality wine red
#Objetivo: Analizar y clasificar la calidad del vino tinto con base a sus atributos
#Atributos: Acidez fija, Acidez volátil, Ácido cítrico, Azúcar residual, 
#Cloruros, Dióxido de azufre libre, Dióxido de azufre libre total, Densidad
# pH, Sulfatos y Alcohol.
#Tipo de dato: Todos son float excepto la calidad que es tipo int.
#Etiqueta: Calidad.
#Una de las problematicas puede ser que hay mas vinos con calidad media que alta o baja
# los datos no estan bien balanceados y podria sesgar los modelos de clasificacion.

atributos = [
    "Acidez fija", "Acidez volátil", "Ácido cítrico",
    "Azúcar residual", "Cloruros", "Dióxido de azufre libre",
    "Dióxido de azufre libre total", "Densidad", "pH", "Sulfatos", "Alcohol"
]

baja =0
media=0
alta=0

with open("winequality-red.csv", "r") as archivo:
    
    lineas = archivo.readlines()  
    lineas = lineas[1:]
    
    for linea in lineas:
        linea = linea.strip()
        
        if linea:
           datos = linea.split(";")
           calidad = int(float(datos[-1]))
           
           print("\nVino analizado:")
           for i in range(len(atributos)):
               print(f"{atributos[i]}: {datos[i]}")
               print(f"-> Calidad: {calidad}\n")
               
        
               if calidad <= 5:
                   print("Vino de baja calidad (", calidad, ")") 
                   baja +=1
               elif calidad == 6:
                   print("Vino de calidad media (", calidad, ")")
                   media +=1
               else:
                   print("Vino de alta calidad (", calidad, ")")
                   alta +=1
            
            
