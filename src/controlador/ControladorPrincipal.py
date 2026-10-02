from src.modelo.Conexion.spark_session import create_spark_session
from src.modelo.Conexion.Conexion import Conexion
from src.modelo.Ejercicios.ejercicio1_a import ejercicio1a
from src.modelo.Ejercicios.ejercicio1_b import ejercicio1b
from src.modelo.Ejercicios.ejercicio1_c import ejercicio1c
from src.modelo.Ejercicios.ejercicio2_a import ejercicio2a
from src.modelo.Ejercicios.ejercicio2_b import ejercicio2b
from src.modelo.Ejercicios.ejercicio3 import ejercicio3a
from src.modelo.Ejercicios.ejercicio4 import ejercicio4
from src.modelo.Ejercicios.ejercicio5 import ejercicio5

RUTA_CSV = "data/ibex35_close-2024.csv"

def ControladorPrincipal():
    print(">>> Controlador iniciado")
    path = r".\lib\mssql-jdbc-13.4.0.jre11.jar"
    spark_session = create_spark_session(path)
    conexion = Conexion(usuario="sa", password="olacaracola")

    df_csv = (
        spark_session.read
        .option("header", True)
        .option("sep", ";")
        .csv(RUTA_CSV)
    )
    conexion.escribir_tabla(df_csv, "Datos2024", "overwrite")
    print(">>> Datos2024 guardada")


    ejercicio1a(spark_session)
    df = ejercicio1b(spark_session)
    df = ejercicio1c(df)

    df = ejercicio2a(df)
    df = ejercicio2b(df)
    df = ejercicio3a(df)

    conexion.escribir_tabla(df.drop("Deficiency Notice UNI"), "Datos2024_mod", "overwrite")
    
    ejercicio4(df)
    df = ejercicio5(df)

    spark_session.stop()



if __name__ == "__main__":
    ControladorPrincipal()