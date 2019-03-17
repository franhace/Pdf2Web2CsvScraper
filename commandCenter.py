import csv
from pdfScrap import extraer_todos_dni

def iterar_dnis():
    lista_dnis = (extraer_todos_dni('', 2, 3))
