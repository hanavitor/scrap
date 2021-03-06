import requests_html as rh
import re
import sys
import time
import newspaper as nw
import utils as u
import visitedlinks as v

session = rh.HTMLSession()
vl = v.VistedLinks()
links = []
i = 0
k = 1

while i<=3210:
    print("Page "+str(k)+" out of 322")
    r = session.get('https://www.cidades.gov.br/ultimas-noticias?start='+str(i))
    print(r.url)
    rl = r.html.find('h2.tileHeadline')
    for link in rl:
        links.extend(link.find('a'))
    links = u.link_return(links)
    for j,link in enumerate(links):
        try:
            print(link)
            print("Link " +str(j)+" of page " +str(k))
            if vl.repeated_links("https://www.cidades.gov.br"+link):
                print("Link already scraped")
                continue
            article = nw.Article("https://www.cidades.gov.br"+link)
            article.download()
            article.parse()
            vl.add_link("https://www.cidades.gov.br"+link)
        except nw.article.ArticleException:
            print("Download failed, see failed.out")
            with open("failed.out", 'a') as f:
                f.write("https://www.cidades.gov.br"+link+"\n")
                continue
            break
        with open(sys.argv[1],'a') as f:
            text = re.sub("\\n\\n","\\n",article.text)
            f.write(text+"\n")
    links.clear()
    i = i+10
    k = k+1
