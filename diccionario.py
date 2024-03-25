# Nuevo diccionario con información personal
informacion_personal = {
    "nombre": "Juan",
    "ciudad": "Ciudad A",
    "profesion": "Ingeniero"
}

# Modificar la ciudad
informacion_personal["ciudad"] = "Ciudad B"

# Agregar la profesión
informacion_personal["profesion"] = "Desarrollador"

# Verificar y agregar el número de teléfono
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "555-1234"

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)

