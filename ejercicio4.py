from pyspark.sql import SparkSession 
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from spark_session import spark_session

#Ej4 'Variación anual' -> ((diferencia/inicial) * 100)
# Bajada Fuerte (=<-15%), Bajada, Neutra (1%), Subida, Subida Fuerte (=>15%)
