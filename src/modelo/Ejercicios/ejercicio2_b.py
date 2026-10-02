from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

#Ej2-b
def ejercicio2b(df):
    print("Ej2-b")
    dates = df.agg(
        min("Fecha").alias("Fecha inicial"),
        max("Fecha").alias("Fecha final")
    )
    dates.show()

    dias = df.select("Fecha").distinct().count()

    print("Días de los que se tiene información: ", dias)

    print("Es muy coherente que haya información de 255 días de 1 año ya que el mercado de la bolsa cierra fines de semana y festivos por lo que no habrá datos de cotización de esos días.")
    print("Se podrían consultar las fechas de las que no se tienen datos para ver si realmente corresponden a esos días no laborables.")
    return df