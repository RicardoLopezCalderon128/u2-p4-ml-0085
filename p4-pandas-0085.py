import pandas as pd
import numpy as np 

n_filas=5
n_columnas=5
tag_columna=tuple("ABCDE")
print(tag_columna)
matriz=np.random.randint( 1,6, size =( n_filas, n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
df = pd.DataFrame (matriz,columns=tag_columna)
print("--- La tabla de data frame --- NC=0085")
print(df)
print("programa echo por ricardo Lopez nc = 0085")