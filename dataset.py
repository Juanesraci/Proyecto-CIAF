# Se importan las librerias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Se establece la ruta de la imagen y su respectivo llamado
agua_filepath = r"/home/juanerc/Documentos/CIAF IA/Proyecto/Agua.csv"
agro_filepath = r"/home/juanerc/Documentos/CIAF IA/Proyecto/Agropecuario.csv"

# Se almacena en una variable los datasets
agua = pd.read_csv(agua_filepath)
agro = pd.read_csv(agro_filepath)

# Se almacena en una variable los valores para graficar
irca = agua['IRCA']
cant_datos = np.arange(len(agua))

# Se genera la grafica
plt.figure(figsize = (10,5))
plt.subplot(1, 2, 1)
plt.scatter(cant_datos, irca, color = 'purple')
plt.subplot(1, 2, 2)
plt.hist(irca, bins = 20, color = 'Indigo')
plt.show()
print(cant_datos)