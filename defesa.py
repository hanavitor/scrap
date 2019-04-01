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
timeout = 2
retry = 0
i = 0
k = 1

open(sys.argv[1],'w')

while i<=3500:
    print("Page "+str(k)+" out of 505")
    r = session.get('http://defesa.gov.br/noticias?start='+str(i))
    print(r.url)
    rl = r.html.find('h2.tileHeadline')
    for link in rl:
        links.extend(link.find('a'))
    links = u.link_return(links)
    for j,link in enumerate(links):
        print(link)
        print("Link " +str(j)+" of page " +str(k))
        if vl.repeated_links("https://defesa.gov.br"+link):
            print("Link already scraped")
            continue
        vl.add_link("https://trabalho.gov.br"+link)
        article = nw.Article("http://defesa.gov.br"+link)
        article.download()
        article.parse()
        #while True:
        #    print(j)
        #    print(link)
        #    try:
        #        time.sleep(timeout)
        #        article.download()
        #        article.parse()
        #    except nw.article.ArticleException:
        #        print("erro")
        #        timout = timeout+1
        #        retry = retry+1
        #        if retry == 3:
        #            retry = 0
        #            timeout = 2
        #            break
        #        continue
        #    break
        with open(sys.argv[1],'a') as f:
            f.write(article.text)
    links.clear()
    i = i+10
    k = k +1
