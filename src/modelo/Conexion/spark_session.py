from pyspark.sql import SparkSession

def create_spark_session(self):

    jar_session = None

    spark_session = (
        SparkSession
        .builder
        .appName("IBEX35")
        .getOrCreate()
        .config('spark.driver.extraClassPath', self.path) \
        )
    
    return spark_session

#spark_session = create_spark_session()