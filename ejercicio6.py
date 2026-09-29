from pyspark.sql import SparkSession 
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from spark_session import spark_session

#Ej6 'NombreEmpresaCambioSignificativo' -> Calcular variación de cada acción de un día a otro