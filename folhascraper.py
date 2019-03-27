from utils import folhaloop, linkreturn, newsloop
from requests_html import HTML, HTMLSession
import os

session = HTMLSession()

r = session.get('https://www.folha.uol.com.br')

hlinks = r.html.find('a.c-headline__url')
slinks = r.html.find('a.c-list-links__url')
hlinks.extend(slinks)

newsloop(linkreturn(hlinks), "b.out")
