from utils import folhaloop, linkreturn 
from requests_html import HTML, HTMLSession
import re
import os
session = HTMLSession()

r = session.get('https://www1.folha.uol.com.br/ultimas-noticias/')

lista = r.html.find('div.c-newslist' , first=True)
links = lista.find('a')

folhaloop(linkreturn(links), "test.out")
