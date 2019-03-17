from bs4 import BeautifulSoup
import requests

url = "tinyurl"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')




def limpiar_string_url(a):
    x = []
    response = requests.get(a)
    soup = BeautifulSoup(response.text, 'html.parser')
    # response = requests.post(url)
    # soup = BeautifulSoup(response.text, 'html.parser')

    for string in soup.stripped_strings:
        x.append(repr(string))
    return x


xx = limpiar_string_url(url)
print(xx)

def nombre_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[13:w])
    return target

print(nombre_completo(xx[6]))



def fono_completo():
    row_tags = soup.findAll("td", {'class': "td-registro"})[18]
    x = []
    for string in row_tags:
        x.append(repr(string))
    fono_tag_grande = (x[1])
    if "v" in fono_tag_grande:
       for i, j in enumerate(fono_tag_grande):
           if j == "v":
               tel = fono_tag_grande[i+7:len(fono_tag_grande)-3]
    return tel


def email_completo():
    row_tags = soup.findAll("td", {'class': "td-registro"})[20]
    x = []
    for string in row_tags:
        x.append(repr(string))
    fono_tag_grande = (x[1])
    if "v" in fono_tag_grande:
       for i, j in enumerate(fono_tag_grande):
           if j == "v":
               email = fono_tag_grande[i+7:len(fono_tag_grande)-3]
    return email


def dom_completo():
    row_tags = soup.findAll("td", {'class': "td-registro"})[12]
    x = []
    domicilio = []
    for string in row_tags:
        x.append(repr(string))
    target1 = (x[1])
    if "v" in target1:
       for i, j in enumerate(target1):
           if j == "v":
               calle = target1[i+7:len(target1)-3]
               domicilio.append(calle)
    target2 = (x[5])
    if "v" in target2:
       for i, j in enumerate(target2):
           if j == "v":
               altura = target2[i+7:len(target2)-3]
               domicilio.append(altura)
    dom_final = ", ".join(domicilio)
    return dom_final


def dom_completo2():
    row_tags = soup.findAll("td", {'class': "td-registro"})[12]
    x = []
    domicilio2 = []
    for string in row_tags:
        x.append(repr(string))
    target1 = (x[9])
    if "v" in target1:
       for i, j in enumerate(target1):
           if j == "v":
               piso = target1[i+7:len(target1)-3]
               domicilio2.append(piso)
    target2 = (x[13])
    if "v" in target2:
       for i, j in enumerate(target2):
           if j == "v":
               dto = target2[i+7:len(target2)-3]
               domicilio2.append(dto)
    dom_fin2 = "".join(domicilio2)
    return dom_fin2


def sexo_completo(casilla):
    w = len(casilla) - 1
    target = (casilla[1:w])
    return target
# print(datos)

def estado_civil(casilla):
    w = len(casilla) - 1
    target = (casilla[1:w])
    return target


def fecha_nacimiento(casilla):
    w = len(casilla) - 1
    target = (casilla[1:w])
    return target

def pais_nacimiento(casilla):
    w = len(casilla) - 1
    target = (casilla[1:w])
    return target

def provincia_nacimiento(casilla):
    w = len(casilla) - 1
    target = (casilla[1:w])
    return target

# Toma string limpio desde distintas urls para cada categoria
# Cual home , cual datosPer
def datear_url(w, z):
    x = w
    xy = z
    data = []
    casilla_nombre = xy
    data.append(nombre_completo(casilla_nombre))
    casilla_sexo = x[7]
    data.append(sexo_completo(casilla_sexo))
    data.append(dom_completo())
    data.append(dom_completo2())
    data.append(fono_completo())
    data.append(email_completo())
    casilla_civil = x[9]
    data.append(estado_civil(casilla_civil))
    casilla_nac = x[11]
    data.append(fecha_nacimiento(casilla_nac))
    casilla_pais = x[16]
    data.append(pais_nacimiento(casilla_pais))
    casilla_provincia = x[18]
    data.append(provincia_nacimiento(casilla_provincia))

    return data


print(datear_url(xx))

