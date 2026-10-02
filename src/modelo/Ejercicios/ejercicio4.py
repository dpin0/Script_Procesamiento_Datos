from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

def ejercicio4(df):
    spark = SparkSession.builder.getOrCreate()

    fecha = "Dia" if "Dia" in df.columns else "Fecha"

    # quito fecha y Deficiency
    empresas = [
        c for c in df.columns
        if c not in ("Fecha", "Dia") and not c.startswith("Deficiency")
    ]

    datos = []
    for c in empresas:
    
        validos = df.select(col(f"`{c}`").cast("double").alias("v")).dropna().orderBy(col(fecha).asc())
        
        if validos.count() == 0:
            continue
        
        inicial = validos.first()["v"]
        final = validos.orderBy(col(fecha).desc()).first()["v"]

        if inicial == 0:
            continue
        
        variacion = ((final - inicial) / inicial) * 100
        datos.append((c, inicial, final, variacion))

    schema_ = StructType([
        StructField("Empresa", StringType(), True),
        StructField("Inicial", DoubleType(), True),
        StructField("Final", DoubleType(), True),
        StructField("Variación Anual", DoubleType(), True)
    ])
    resultado = spark.createDataFrame(datos, schema=schema_)

    resultado = resultado.withColumn(
        "Clasificación",
        when(col("Variación Anual") >= 15, "Subida Fuerte")
        .when(col("Variación Anual") <= -15, "Bajada Fuerte")
        .when(col("Variación Anual") >= 1, "Subida")
        .when(col("Variación Anual") <= -1, "Bajada")
        .otherwise("Neutra")
    )

    resultado.show(30, truncate=False)
    return resultado