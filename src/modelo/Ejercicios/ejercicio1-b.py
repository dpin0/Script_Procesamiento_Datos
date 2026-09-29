from pyspark.sql import SparkSession 
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from spark_session import spark_session


#Carga de los datos del CSV en DataFrame de PySpark
df = spark_session.read.option("header", True).option("sep", ';').option("dateFormat","dd/MM/yyyy").csv('ibex35_close-2024.csv')

#Ej1-b
#eliminar sufijo .MC de los nombres de cada columna

for i in df.columns:
    nuevo_nombre = i.replace(".MC", "")
    df = df.withColumnRenamed(i, nuevo_nombre)

df.show(6)
