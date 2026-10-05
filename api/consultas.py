import pandas as pd
from sodapy import Socrata

def consultar_departamento():
    nombre_departamento = str(input("Departamento:\n")).upper()
    limite_registros = str(input("registros:\n"))
    # Cliente sin autenticación (solo datasets públicos)
    client = Socrata("www.datos.gov.co", None)



    # Filtro usando SoQL (where)
    results = client.get(
        "gt2j-8ykr",
        limit=limite_registros,
        where=f"departamento_nom='{nombre_departamento}'"
    )

    results_df = pd.DataFrame.from_records(results)
    print(results_df.head())
