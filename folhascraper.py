from requests_html import HTML, HTMLSession
import re

session = HTMLSession()
r = session.get('https://www.folha.uol.com.br')

hlinks = r.html.find('a.c-headline__url')
slinks = r.html.find('a.c-list-links__url')
hlinks.extend(slinks)
links = []

for link in hlinks:
    links.append(link.attrs['href'])

for link in links:
    if re.search("www1\.folha\.uol\.com\.br", link):
        print(link)
        rl = session.get(link)
        news = rl.html.find('div.c-news__body', first = True)
        
        paragraphs = news.find('p')
        
        with open('file.out', 'a') as f:
            for paragraph in paragraphs:
                if paragraph.text == '':
                    continue
                f.write(paragraph.text + "\n")
