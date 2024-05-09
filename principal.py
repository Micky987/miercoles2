import operaciones

ruta = r"C:\Users\estudiante\Desktop\miercoles\martespy-main\archivo\ventas.csv"
nueva_venta = { 
        "id" : 0,
        "codigo_cliente": 10009,
        "cliente": "Gabriel Casas",
        "producto":"Papas fritas",
        "precio": 68,
        "descuento": "",
        "iva": ""
}

#operaciones.registrar_csv(nueva_venta, ruta)


lectura = True
while lectura:
    accion = input('Accion:  ')
    if (accion == 'nuevo'):
        # leer los procuttos
        codigo_cliente = input('Codigo Cliente:')
        cliente = input('Cliente:')
        producto = input('Producto:')
        precio = input('Precio:')

        nueva_venta = {
            'id': 0,
            'codigo_cliente': codigo_cliente,
            'cliente': cliente,
            'producto': producto,
            'precio': precio,
            'descuento': '',
            'iva': ''
        }
        operaciones.registrar_csv(nueva_venta, ruta)
    else:
        lectura = False
        # break
