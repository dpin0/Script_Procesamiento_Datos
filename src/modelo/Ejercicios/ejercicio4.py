from pyspark.sql.functions import *
from pyspark.sql.window import Window


def ejercicio4(df):
    spark_session = df.sparkSession

    fecha = "Dia" if "Dia" in df.columns else "Fecha"

    empresas = [
        c for c in df.columns
        if c not in ("Fecha", "Dia")
        and not c.startswith("Deficiency")
    ]

    filas = []

    for c in empresas:
        datos = (
            df.select(col(fecha),
                col(f"`{c}`").cast("double").alias("valor")
            )
            .dropna(subset=["valor"])
        )

        primera = (datos.orderBy(col(fecha).asc()).first())
        ultima = (datos.orderBy(col(fecha).desc()).first())

        if primera is None or ultima is None:
            print(f">>> {c}: sin datos")
            continue

        ini = primera["valor"]
        fin = ultima["valor"]
        if ini == 0:
            continue

        variacion = ((fin - ini) / ini) * 100

        filas.append((c,float(ini),float(fin),float(variacion)))

    print(f">>> Empresas procesadas: {len(filas)}")

    if not filas:
        print(">>> No hay resultados para crear")
        return df

    resultado = spark_session.createDataFrame(
        filas,
        ["Empresa", "Inicial", "Final", "Variación Anual"]
    )

    resultado = resultado.withColumn(
        "Clasificación",
        when(col("Variación Anual") >= 15, "Subida Fuerte")
        .when(col("Variación Anual") <= -15, "Bajada Fuerte")
        .when(col("Variación Anual") >= 1, "Subida")
        .when(col("Variación Anual") <= -1, "Bajada")
        .otherwise("Neutra")
    )
    
    '''
    USO DE IA: Chat GPT -> no conseguí que funcionase resultado.show(truncate = False) y lo usé
    para generar un print que mostrase por pantalla la tabla resultado
    '''
    print(">>> RESULTADO EJERCICIO 4")
    print("Empresa | Inicial | Final | Variación Anual | Clasificación")
    
    for fila in filas:
        empresa, inicial, final, variacion = fila

        if variacion >= 15:
            clasificacion = "Subida Fuerte"
        elif variacion <= -15:
            clasificacion = "Bajada Fuerte"
        elif variacion >= 1:
            clasificacion = "Subida"
        elif variacion <= -1:
            clasificacion = "Bajada"
        else:
            clasificacion = "Neutra"

        print(
            f"{empresa} | "
            f"{inicial:.2f} | "
            f"{final:.2f} | "
            f"{variacion:.2f}% | "
            f"{clasificacion}"
        )

    return resultado