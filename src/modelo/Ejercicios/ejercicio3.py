from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

#Ej3-a
def ejercicio3a(df):

    #'Fecha' -> 'Día'
    df = df.withColumnRenamed("Fecha", "Dia")
    df.show(10)

    #media, max y min
    empresas = [c for c in df.columns if c != "Dia"]
    expresiones = []
    for c in empresas:
        expresiones.append(avg(col(f"`{c}`")).alias(f"Media anual {c}"))
        expresiones.append(max(col(f"`{c}`")).alias(f"Max anual {c}"))
        expresiones.append(min(col(f"`{c}`")).alias(f"Min anual {c}"))
    df.agg(*expresiones).show(truncate=False)


    df = df.withColumn(
        "Deficiency Notice UNI",
        when(col("UNI") < 1, True).otherwise(False)
    )
    df.show(100)

    return df