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

while i<=999:
    print("Page "+str(k)+" out of 112")
    r = session.get('http://mds.gov.br/area-de-imprensa/area-de-imprensa/noticias?b_start:int='+str(i))
    print(r.url)
    rl = r.html.find('h2.tileHeadline')
    for link in rl:
        links.extend(link.find('a.summary.url'))
    links = u.link_return(links)
    for j,link in enumerate(links):
        try:
            print(link)
            print("Link " +str(j)+" of page " +str(k))
            if vl.repeated_links(link):
                print("Link already scraped")
                continue
            article = nw.Article(link)
            article.download()
            article.parse()
            vl.add_link(link)
        except nw.article.ArticleException:
            print("Download failed, see failed.out")
            with open("failed.out", 'a') as f:
                f.write(link)
                continue
            break
        with open(sys.argv[1],'a') as f:
            text = re.sub("\\n\\n","\\n",article.text)
            f.write(text+"\n")
    links.clear()
    i = i+9
    k = k +1
