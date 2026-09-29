from pyspark.sql import SparkSession 
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from spark_session import spark_session

#Ej2-a
data_frame.select(countDistinct("namecol"))
data_frame.distinct()
