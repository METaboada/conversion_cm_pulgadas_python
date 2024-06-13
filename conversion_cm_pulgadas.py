
# Paso1: Solicitar al usuario las medidas de las piezas del mueble en cm
medida_en_centimetros = float(input("Por favor, ingresar las medidas de la pieza del mueble en centímetros: "))

# Paso2: Convertir las medidas de cm a pulgadas
media_en_pulgadas = medida_en_centimetros / 2.54

# Paso3: Mostrar las medidas convertidas en pulgadas al usuario
print ("Las medidas en pulgadas de la pieza ingresada son", media_en_pulgadas, "pulgadas")


