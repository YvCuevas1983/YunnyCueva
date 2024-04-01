import os

# Escritura de Archivo de Texto:
with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Esta es mi primera nota.\n")
    file.write("Nota 2: Este es mi segundo pensamiento.\n")
    file.write("Nota 3: ¡No puedo esperar a compartir más notas!\n")

# Lectura de Archivo de Texto:
with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Cierre de Archivos:
file.close()