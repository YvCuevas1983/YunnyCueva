import numpy as np

# Definir nombres de ciudades, días de la semana y semanas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']

# Crear una matriz 3D de 3 ciudades, 7 días de la semana y 4 semanas
# Aquí se generan valores aleatorios para las temperaturas
# Puedes sustituir estos valores con los datos reales
temperaturas = np.random.randint(0, 40, size=(len(ciudades), len(dias_semana), len(semanas)))

# Mostrar las matrices de temperaturas con los días asociados
print("Matrices de temperaturas:")
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    print("\t" + "\t".join(dias_semana))
    for semana_idx, semana in enumerate(semanas):
        print(f"{semana}:")
        for dia_idx, dia in enumerate(dias_semana):
            print(dia + ":", temperaturas[ciudad_idx, dia_idx, semana_idx], "°C", end="\t")
        print()

# Calcular el promedio de temperaturas para cada ciudad por semana
print("\nPromedio de temperaturas:")
for ciudad_idx, ciudad in enumerate(ciudades):
    for semana_idx, semana in enumerate(semanas):
        promedio_semana = np.mean(temperaturas[ciudad_idx, :, semana_idx])
        print(f"Promedio de temperaturas para {ciudad} en {semana}: {promedio_semana:.2f}°C")
