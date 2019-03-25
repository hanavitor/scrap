from requests_html import HTML, HTMLSession
from newsplease import NewsPlease
session = HTMLSession()

def folhaloop(links, tfile):
    for i,link in enumerate(links):
        print(link)
        print("Article "+str(i)+" out of "+str(len(links)))
        rl = session.get(link)
        news = rl.html.find('div.c-news__body', first = True)
    
        if isinstance(news,type(None)):
            print("Page out of scope, see exceptions.out")
            with open('exceptions.out', 'a') as f:
                f.write(link + "\n")
            continue
    
        paragraphs = news.find('p')
    
        with open(tfile, 'a') as f:
            for paragraph in paragraphs:
                if paragraph.text == '':
                    continue
                f.write(paragraph.text + "\n")

def linkreturn(hlinks):
    links = []
    for i,link in enumerate(hlinks):
        links.append(link.attrs['href'])
        if i > 0 and links[-1] == links[-2]:
            links.pop()
    return links

def newsloop(links, tfile):
    for i,link in enumerate(links):
        print(link)
        print("Article "+ str(i) +" out of "+str(len(links)))
        article = NewsPlease.from_url(link)
        if article.text == None:
            print("out of scope haha")
            continue
        with open(tfile, 'a') as f:
            f.write(article.text)
