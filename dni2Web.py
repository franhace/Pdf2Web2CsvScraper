import mechanicalsoup
from pdfScrap import extraer_todos_dni
import argparse
from bs4 import BeautifulSoup
import urllib
import bs4
from requests import request
import requests

# parser = argparse.ArgumentParser(
#     description="Login to tinyurl")

lista_dnis = (extraer_todos_dni('filename', 3, 4))


browser = mechanicalsoup.StatefulBrowser()

browser.open("tinyurl")

print(browser.get_url())
a = "11111111"

def get_id(dni):
    browser = mechanicalsoup.Browser(soup_config={'features': 'html.parser'})
    loginPage = browser.get('tinyurl')
    form = loginPage.soup.find_all('form')[0]
    form.find("input", {"name": "usuario"})["value"] = dni
    form.find("input", {"name": "contrasegna"})["value"] = dni
    page = browser.submit(form, loginPage.url)
    b = (page.text)
    if b[35] != "R":
        print("Todo bien por aqui")
        return b[165:195]
    else:
        print("Problema de login")

print(get_id(1111111))

def confirmar_dnis(l):
    l1 = []
    for i in l:
        a = get_id(i)
        l1.append(a)

    return l1

print(confirmar_dnis(lista_dnis))

# def get_name(id):
# def get_todos(id):

# login_response = browser.submit(login_form, login_page.url)
# messages = login_response.soup.find("div", class_="flash-messages")
# if messages:
#     print(messages.text)
# # assert page2.soup.select(".logout-form")
# #
# # print(page2.soup.title.text)