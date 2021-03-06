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

while i<=3500:
    print("Page "+str(k)+" out of 351")
    r = session.get('https://www.defesa.gov.br/noticias?start='+str(i))
    print(r.url)
    rl = r.html.find('h2.tileHeadline')
    for link in rl:
        links.extend(link.find('a'))
    links = u.link_return(links)
    for j,link in enumerate(links):
        try:
            print(link)
            print("Link " +str(j)+" of page " +str(k))
            if vl.repeated_links("https://www.defesa.gov.br"+link):
                print("Link already scraped")
                continue
            article = nw.Article("https://www.defesa.gov.br"+link)
            article.download()
            article.parse()
            vl.add_link("https://www.defesa.gov.br"+link)
        except nw.article.ArticleException:
            print("Download failed, see failed.out")
            with open("failed.out", 'a') as f:
                f.write("https://www.defesa.gov.br"+link)
                continue
            break
        with open(sys.argv[1],'a') as f:
            text = re.sub("\\n\\n","\\n",article.text)
            f.write(text+"\n")
    links.clear()
    i = i+10
    k = k +1
