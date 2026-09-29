from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

#Ej1-c
def ejercicio1c(spark_session):

    #definir strucType (tipo de dato/ columna y nombre o siglas/ empresa)
    schema = StructType([
        StructField("Fecha", DateType(), True),
        StructField("Iberdrola", DecimalType(10, 2), True),
        StructField("Repsol", DecimalType(10, 2), True),
        StructField("Naturgy", DecimalType(10, 2), True),
        # Uso de IA: Claude para crear el resto de StructFields de las empresas
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

    return df_c