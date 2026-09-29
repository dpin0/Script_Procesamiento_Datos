from pyspark.sql import SparkSession

spark_session = (SparkSession.builder.appName("IBEX35").getOrCreate())
