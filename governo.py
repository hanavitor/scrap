import requests_html as rh
import re
import sys
import time
import newspaper as nw
import utils as u
import visitedlinks as v

session = rh.HTMLSession()
vl = v.VistedLinks()
flag = True
links = []
timeout = 2
retry = 0
i = 1

open(sys.argv[1],'w')

while i<=203:
    print("Page "+str(i)+" out of 203")
    r = session.get('http://ctav.gov.br/category/noticias/page/'+str(i))
    print(r.url)
    rl = r.html.find('h2.entry-title')
    for link in rl:
        links.extend(link.find('a'))
    links = u.link_return(links)
    for j,link in enumerate(links):
        print(link)
        print("Link " +str(j)+" of page " +str(i))
        if vl.repeated_links(link):
            print("Link already scraped")
            continue
        vl.add_link(link)
        article = nw.Article(link)
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
            text = re.sub("\\n\\n","\\n",article.text)
            f.write(text+"\n")
    links.clear()
    i = i+1
