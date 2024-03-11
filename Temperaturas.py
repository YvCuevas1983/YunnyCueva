import numpy as np

def calcular_temperatura_promedio(ciudades, dias_semana, semanas, temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Args:
    - ciudades (list): Lista de nombres de ciudades.
    - dias_semana (list): Lista de días de la semana.
    - semanas (list): Lista de semanas.
    - temperaturas (numpy.ndarray): Matriz 3D de temperaturas.

    Returns:
    - dict: Diccionario que contiene el promedio de temperatura por ciudad y semana.
    """
    promedios = {}
    for ciudad_idx, ciudad in enumerate(ciudades):
        promedios[ciudad] = {}
        for semana_idx, semana in enumerate(semanas):
            promedio_semana = np.mean(temperaturas[ciudad_idx, :, semana_idx])
            promedios[ciudad][semana] = round(promedio_semana, 2)
    return promedios

# Definir nombres de ciudades, días de la semana y semanas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']

# Crear una matriz 3D de 3 ciudades, 7 días de la semana y 4 semanas
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
promedios = calcular_temperatura_promedio(ciudades, dias_semana, semanas, temperaturas)
print("\nPromedio de temperaturas:")
for ciudad, semana_temperaturas in promedios.items():
    for semana, promedio in semana_temperaturas.items():
        print(f"Promedio de temperaturas para {ciudad} en {semana}: {promedio}°C")
