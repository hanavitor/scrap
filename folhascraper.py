from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://www1.folha.uol.com.br/mundo/2019/03/homenageado-por-bannon-olavo-de-carvalho-diz-desconhecer-ideias-politicas-de-bolsonaro.shtml')

news = r.html.find('div.c-news__body', first = True)

paragraphs = news.find('p')

with open('file.out', 'w') as f:
    for paragraph in paragraphs:
        if paragraph.text == '':
            continue
        f.write(paragraph.text + "\n")
