from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *


def ejercicio3(df):

    #Ej3-a
    print("Ej3-a")
    #'Fecha' -> 'Día'
    df = df.withColumnRenamed("Fecha", "Dia").orderBy("Dia")
    df.show(10)

    #media, max y min
    empresas = [c for c in df.columns if c != "Dia"]
    expresiones = []
    for c in empresas:
        expresiones.append(avg(col(f"`{c}`")).alias(f"Media anual {c}"))
        expresiones.append(max(col(f"`{c}`")).alias(f"Max anual {c}"))
        expresiones.append(min(col(f"`{c}`")).alias(f"Min anual {c}"))
    df.agg(*expresiones).show(truncate=False)


    df = df.withColumn(
        "Deficiency Notice UNI",
        when(col("UNI") < 1, True).otherwise(False)
    )
    df.show(100)

    print("Ej3-b")
    print("La selección de empresas del IBEX35 se basa en criterios de liquidez y capitalización bursátil.")
    print("Referencia: https://www.elclubdeinversion.com/ufaq/como-se-seleccionan-las-empresas-que-forman-parte-del-ibex-35/")
    print("Los datos con NULL son por el cambio de la empresa Meliá Hotels por Puig Brands en el IBEX a mediados de julio 2024.")
    print("Referencia:https://www.eleconomista.es/mercados-cotizaciones/noticias/12902703/07/24/puig-entra-al-ibex-35-por-melia-tan-solo-dos-meses-despues-de-su-salida-a-bolsa.html")
    print("Los NULL no afectan si se omiten en los cálculos de cada empresa.")
    
    return df