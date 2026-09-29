from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *


#Ej6 'NombreEmpresaCambioSignificativo' -> Calcular variación de cada acción de un día a otro

def ejercicio6(spark_session):
    
    #Carga de los datos del CSV en DataFrame de PySpark
    df = (
        spark_session.read
        .option("header", True)
        .option("sep", ';')
        .option("dateFormat","dd/MM/yyyy")
        .csv('ibex35_close-2024.csv')
    )