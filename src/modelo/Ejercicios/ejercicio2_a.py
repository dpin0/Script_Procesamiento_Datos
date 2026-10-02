from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

#Ej2-a
def ejercicio2a(df):
    
    filas_0 = df.count()
    df = df.dropDuplicates()
    filas_1 = df.count()

    filas_borradas = filas_0 - filas_1
    print("Filas eliminadas:", filas_borradas)

    #N de empresas
    n_empresas = len(df.columns) - 1 #para quitar la fecha

    print("Empresas de las que se tiene información:", n_empresas)

    return df