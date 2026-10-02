from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *


def ejercicio5(df):
    df = df.dropDuplicates()

    # quito fecha y Deficiency
    empresas = [
        c for c in df.columns
        if c not in ("Fecha", "Dia") and not c.startswith("Deficiency")
        and not c.endswith("Cuartil")
    ]

    for c in empresas:
        nombre = c.replace(".MC", "")
        q1, q2, q3 = df.approxQuantile(f"`{c}`", [0.25, 0.5, 0.75], 0.01)
        df = df.withColumn(
            f"{nombre}Cuartil",
            when(col(f"`{c}`").isNull(), lit(None))
            .when(col(f"`{c}`") <= q1, "q1")
            .when(col(f"`{c}`") <= q2, "q2")
            .when(col(f"`{c}`") <= q3, "q3")
            .otherwise("q4")
        )

    print(df.head(1)[0])

    df.select(
        col("`AENA.MC`"), col("AENACuartil"),
        col("`BBVA.MC`"), col("BBVACuartil")
    ).show(df.count(), truncate=False)
    
    return df