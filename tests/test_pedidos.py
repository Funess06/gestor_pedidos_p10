from pedidos import calcular_totales_pedido


def test_calcular_totales_sin_descuento():
    # Preparamos unos datos falsos (1 producto de 10€)
    lineas_prueba = [{"producto": "Ratón", "cantidad": 1, "precio": 10.0}]

    # Ejecutamos nuestra función
    resultado = calcular_totales_pedido(lineas_prueba)

    # Comprobamos que las matemáticas son correctas
    assert resultado["subtotal"] == 10.0
    assert resultado["descuento"] == 0.0
    assert resultado["iva"] == 2.10
    assert resultado["total"] == 12.10
