from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

#Ej1-b
def ejercicio1b(spark_session):

    df = (
        spark_session.read
        .option("header", True)
        .option("sep", ';')
        .option("dateFormat","dd/MM/yyyy")
        .csv('ibex35_close-2024.csv')
    )

    #eliminar sufijo .MC de los nombres de cada columna

    for i in df.columns:
        nuevo_nombre = i.replace(".MC", "")
        df = df.withColumnRenamed(i, nuevo_nombre)

    df.show(6)

    return df
