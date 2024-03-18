def calcular_descuento(monto_total, porcentaje_descuento=10):
  descuento = monto_total * porcentaje_descuento / 100
  return descuento
 

# Llamadas a la función calcular_descuento
monto_total_1 = 100
descuento_1 = calcular_descuento(monto_total_1)
print(f"Descuento para una compra de {monto_total_1}: ${descuento_1}")
print(f"Monto final a pagar: ${monto_total_1 - descuento_1}")

monto_total_2 = 200
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
print(
    f"Descuento para una compra de {monto_total_2} con {porcentaje_descuento_2}% de descuento: ${descuento_2}"
)
print(f"Monto final a pagar: ${monto_total_2 - descuento_2}")
