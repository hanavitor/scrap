from requests_html import HTML, HTMLSession
import re
import os

session = HTMLSession()
r = session.get('https://www.folha.uol.com.br')

hlinks = r.html.find('a.c-headline__url')
slinks = r.html.find('a.c-list-links__url')
hlinks.extend(slinks)
links = []

for i,link in enumerate(hlinks):
    links.append(link.attrs['href'])
    if i > 0 and links[-1] == links[-2]:
        links.pop()

if os.path.isfile('a.out'):
        f = open('a.out', 'w')
        f.close()

for link in links:

    print(link)
    rl = session.get(link)
    news = rl.html.find('div.c-news__body', first = True)

    if isinstance(news,type(None)):
        print("Page out of scope, see exceptions.out")
        with open('exceptions.out', 'a') as f:
            f.write(link + "\n")
        continue

    paragraphs = news.find('p')

    with open('a.out', 'a') as f:
        for paragraph in paragraphs:
            if paragraph.text == '':
                continue
            #splits = paragraph.text.split('.')
            #for split in splits:
            #    f.write(split + "\n")
            f.write(paragraph.text + "\n")
