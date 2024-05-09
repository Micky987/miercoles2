import csv 

# with operador que va a operar un archivo 
#           ventas 1 es el excel csv
#                          "r" es read
with open ("ventas1.csv", "r") as archivo:
    datos_csv=csv.DictReader(archivo)
    for fila in datos_csv:
        print(fila)
