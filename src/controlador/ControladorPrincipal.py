from src.modelo.Conexion.spark_session import create_spark_session
from src.modelo.Ejercicios.ejercicio1_a import ejercicio1a
from src.modelo.Ejercicios.ejercicio1_b import ejercicio1b
from src.modelo.Ejercicios.ejercicio1_c import ejercicio1c
from src.modelo.Ejercicios.ejercicio2_a import ejercicio2a
from src.modelo.Ejercicios.ejercicio3 import ejercicio3
from src.modelo.Ejercicios.ejercicio4 import ejercicio4
from src.modelo.Ejercicios.ejercicio5 import ejercicio5
from src.modelo.Ejercicios.ejercicio6 import ejercicio6

def ControladorPrincipal():
    path = r".\lib\mssql-jdbc-13.4.0.jre11.jar"
    spark_session = create_spark_session(path)

    ejercicio1a(spark_session)
    ejercicio1b(spark_session)
    ejercicio1c(spark_session)
    ejercicio2a(spark_session)
    ejercicio3(spark_session)
    ejercicio4(spark_session)
    ejercicio5(spark_session)
    ejercicio6(spark_session)

    spark_session.stop()




if __name__ == "__main__":
    ControladorPrincipal()