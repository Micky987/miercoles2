import csv

def porcentaje (numero, porcentaje=13):
    resultado = numero * (porcentaje / 100) 
    return resultado

def descuento (precio):
    descuento = 0
    if precio > 100:
        descuento = porcentaje(precio, 15)
    else:
        descuento = porcentaje(precio, 5)
    return descuento

def calcular (lista, funcion):
    total = 0
    for producto, precio in lista.items():
        total += funcion(precio)
    return total

def leer_csv (ruta):
    resultado = []
    with open(ruta, 'r') as archivo:
        datos_csv = csv.DictReader(archivo)
        for fila in datos_csv:
            resultado.append(fila)
    return resultado

def registrar_csv (fila, ruta):
    data = leer_csv(ruta)
    id = data[-1]['id']
    id = int(id)
    id += 1
    # id = int(data[-1]['id'])+1
    fila['id'] = id
    with open (ruta, 'a', newline='') as archivo:
        escritura = csv.DictWriter(archivo, fieldnames=fila.keys())
        escritura.writerow(fila)





    