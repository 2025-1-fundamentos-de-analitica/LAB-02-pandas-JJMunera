"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    tbl1 = pd.read_csv("/files/input/tbl1.tsv", sep="\t") 
    unico = tbl1.groupby('c4')['c0'].max().sort_index()
    unico.index = unico.index.str.upper() 
    solo_letras = unico.index.tolist()

    return solo_letras

"""
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
