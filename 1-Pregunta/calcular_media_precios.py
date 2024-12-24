import csv
from collections import defaultdict

# Leer el archivo CSV y calcular la media de los precios
precios = defaultdict(list)
with open('datos.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        precios[row['producto']].append(float(row['precio']))

# Calcular la media de los precios
precios_medios = {producto: sum(precios[producto]) / len(precios[producto]) for producto in precios}

# Escribir el archivo resultado.csv con las columnas 'producto' y 'precio_medio'
with open('resultado.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['producto', 'precio_medio'])
    for producto, precio_medio in precios_medios.items():
        writer.writerow([producto, precio_medio])