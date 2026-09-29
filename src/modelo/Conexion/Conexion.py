from pyspark.sql import SparkSession

path = r".\lib\mysql-connector-j-9.4.0.jar"

spark_session = (
    SparkSession.builder
    .appName("IBEX35")
    .config("spark.driver.extraClassPath", path)
    .getOrCreate()
)