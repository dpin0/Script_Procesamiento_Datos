from pyspark.sql import SparkSession 
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

#Ej1-a
spark_session = (SparkSession.builder.appName("IBEX35").getOrCreate())

#Carga de los datos del CSV en DataFrame de PySpark
df = spark_session.read.option("header", True).option("sep", ';').option("dateFormat","dd/MM/yyyy").csv('ibex35_close-2024.csv')

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

#Ej1-b
#eliminar sufijo .MC de los nombres de cada columna

for i in df.columns:
    nuevo_nombre = i.replace(".MC", "")
    df = df.withColumnRenamed(i, nuevo_nombre)

df.show(6)


#Ej1-c
#definir strucType (tipo de dato/ columna y nombre o siglas/ empresa)

schema = StructType([
    StructField("Fecha", DateType(), True),
    StructField("Iberdrola", DecimalType(10, 2), True),
    StructField("Repsol", DecimalType(10, 2), True),
    StructField("Naturgy", DecimalType(10, 2), True),
    StructField("Endesa", DecimalType(10, 2), True),
    StructField("Enagas", DecimalType(10, 2), True),
    StructField("Redeia", DecimalType(10, 2), True),
    StructField("Santander", DecimalType(10, 2), True),
    StructField("BBVA", DecimalType(10, 2), True),
    StructField("CaixaBank", DecimalType(10, 2), True),
    StructField("Bankinter", DecimalType(10, 2), True),
    StructField("Banco_Sabadell", DecimalType(10, 2), True),
    StructField("Unicaja", DecimalType(10, 2), True),
    StructField("Mapfre", DecimalType(10, 2), True),
    StructField("ACS", DecimalType(10, 2), True),
    StructField("Acciona", DecimalType(10, 2), True),
    StructField("Acciona_Energia", DecimalType(10, 2), True),
    StructField("Acerinox", DecimalType(10, 2), True),
    StructField("ArcelorMittal", DecimalType(10, 2), True),
    StructField("Sacyr", DecimalType(10, 2), True),
    StructField("Cellnex", DecimalType(10, 2), True),
    StructField("Telefonica", DecimalType(10, 2), True),
    StructField("Aena", DecimalType(10, 2), True),
    StructField("Ferrovial", DecimalType(10, 2), True),
    StructField("Inditex", DecimalType(10, 2), True),
    StructField("Amadeus", DecimalType(10, 2), True),
    StructField("IAG", DecimalType(10, 2), True),
    StructField("Grifols", DecimalType(10, 2), True),
    StructField("Fluidra", DecimalType(10, 2), True),
    StructField("Solaria", DecimalType(10, 2), True),
    StructField("Rovi", DecimalType(10, 2), True),
    StructField("Logista", DecimalType(10, 2), True),
    StructField("Indra", DecimalType(10, 2), True),
    StructField("Melia_Hotels", DecimalType(10, 2), True),
    StructField("Puig", DecimalType(10, 2), True),
    StructField("Colonial", DecimalType(10, 2), True),
    StructField("Merlin_Properties", DecimalType(10, 2), True),
])
 
df_c = (spark_session.read
             .option("header", True)
             .option("sep", ';')
             .option("dateFormat", "dd/MM/yyyy")
             .schema(schema)
             .csv('ibex35_close-2024.csv'))

#mostrar estructura y 6 primeras filas
df_c.printSchema()
df_c.show(6)


#Ej2-a
data_frame.select(countDistinct("namecol"))
data_frame.distinct()