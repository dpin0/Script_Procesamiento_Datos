from pyspark.sql import SparkSession

def create_spark_session(self):

    spark_session = (
        SparkSession.builder
        .appName("IBEX35")
        .config('spark.driver.extraClassPath', self.path)
        .getOrCreate()
    )
    
    return spark_session

