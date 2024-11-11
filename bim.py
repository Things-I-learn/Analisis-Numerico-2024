# El número en binario con punto decimal "1.11101" representa una fracción binaria.
# Primero, convertimos "1.11101" a su equivalente en decimal.

# Parte entera (1) y parte fraccionaria (0.11101)
integer_part = int("1", 2)
fractional_part = "1111011"

# Convertir la parte fraccionaria a decimal
fractional_value = sum(int(bit) * (2 ** -i) for i, bit in enumerate(fractional_part, 1))

# Sumamos la parte entera y la parte fraccionaria para obtener el número en decimal
binary_decimal_number = integer_part + fractional_value

# Ahora realizamos la operación solicitada: binary_decimal_number * (2 ** 6)
result = binary_decimal_number * (2 ** 6)
print(result)

