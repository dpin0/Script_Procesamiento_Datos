from pyspark.sql import SparkSession 
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from spark_session import spark_session

#Carga de los datos del CSV en DataFrame de PySpark
df = spark_session.read.option("header", True).option("sep", ';').option("dateFormat","dd/MM/yyyy").csv('ibex35_close-2024.csv')

#Ej1-a
#Esquema para comprobar el tipo de cada columna
df.printSchema()

#Convertir 'fecha' de string a date 
df = df.withColumn("Fecha", 
                   regexp_replace(col("Fecha"), r"(\d{2})/(\d{2})/(\d{4})", r"$3-$2-$1"))
df = df.withColumn("Fecha", 
                   col("Fecha").cast("date"))

#Convertir 'precios' de string a num 
columnas_precio = [c for c in df.columns if c != "Fecha"]
for c in columnas_precio:
    df = df.withColumn(c, regexp_replace(col(f"`{c}`"), ",", "."))
    df = df.withColumn(c, col(f"`{c}`").cast("decimal(10, 2)")) 

df.printSchema()
df.show(6)