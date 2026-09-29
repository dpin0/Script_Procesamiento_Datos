from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

#Ej2-b
def ejercicio2b(df):
    dates = df.agg(
        min("Fecha").alias("Fecha inicial"),
        max("Fecha").alias("Fecha final")
    )
    dates.show()

    dias = df.select("Fecha").distinct().count()

    print("Días de los que se tiene información: ", dias)

    return df