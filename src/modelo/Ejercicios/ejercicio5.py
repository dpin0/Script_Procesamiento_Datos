from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *


#Ej5 Calcular distribución de precios de cada empresa
# 'NombreEmpresaCuartil' q1, q2, q3 o q4
def ejercicio5(spark_session):
    
    #Carga de los datos del CSV en DataFrame de PySpark
    df = (
        spark_session.read
        .option("header", True)
        .option("sep", ';')
        .option("dateFormat","dd/MM/yyyy")
        .csv('ibex35_close-2024.csv')
    )

    df.show(1)
