import PyPDF2

# Funcion que desde una lista
# busca los dnis luego de la palabra "DN "
# Actualmente funciona solo para dnis de max 8 digitos
# Sean nac o extranjeros
# Actualizar para dnis de mas largo, agregando 1 caracter mas al final
# y borrando lugar vacio


def encontrar_dni_pag(z, num_pag):
    c = 0
    dnis = []
    letra = 'D'
    if letra in z:
        for i, j in enumerate(z):
            if j == letra:
                try:
                    if z[i+1] == 'N':
                        # print("lugar despues de la N es :{}".format(z[i+2]))
                        # print("'" + palabra + "'", "is in position", i + 1)
                        if z[i+2] == ' ':
                            c += 1
                            w = (z[i+3:i+13])
                            dnis.append(w)
                except IndexError:
                    pass
                continue
    print("hay {} dnis en la pag {}".format(c, num_pag+1))
    return dnis


# Limpar los "." de los dnis y los devuelve en
# una lista todos unidos, llamada lista_limpia

def limpiar_lista_dnis(lista_sucia):
    lista_limpia = []

    for g in lista_sucia:
        for n, i in enumerate(g):
            if i == ".":
                g.remove(i)
        res = "".join(g)
        # print(res)
        lista_limpia.append(res)
    return lista_limpia


# Toma 3 argumentos: un archivo, pagina inicial y pagina final
# abre el archivo
# encuentra_dni_pag y luego limpiar_lista_dnis
# pasa los dnis obtenidos en todas las paginas
# a una lista con todos los dnis


def extraer_todos_dni(file, pag_ini, pag_fin):

    object = open(file, 'rb')
    reader = PyPDF2.PdfFileReader(object)

    # si se pasa el argumento "all", escanea desde primera pagina
    if pag_ini == 'all':
        pag_ini = -1
    # si se pasa el argumento "all", escanea hasta ultima pagina
    if pag_fin == 'all':
        numero_total_pag = reader.numPages
        pag_fin = numero_total_pag-1

    l2 = []  # lista, de listas de dnis
    lista_plana = []  # lista de dnis
    # Genera lista de listas con dnis
    while pag_ini < pag_fin:
        pag_ini += 1
        page = reader.getPage(pag_ini)
        extractor = page.extractText()
        z = list(extractor)
        w = limpiar_lista_dnis(encontrar_dni_pag(z, pag_ini))
        l2.append(w)
    # Junta lista de listas
    for sublist in l2:
        for i in sublist:
            lista_plana.append(i)

    cantidad_dnis = (len(lista_plana))
    print("Hay '{}' dnis almacenados.".format(cantidad_dnis))

    return lista_plana


lista_dnis = (extraer_todos_dni('file', 2, 3))
print(lista_dnis)
