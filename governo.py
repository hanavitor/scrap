import requests_html as rh
import sys
import time
import newspaper as nw
import utils as u

session = rh.HTMLSession()

flag = True
links = []
timeout = 2
retry = 0
i = 0

while i<=390:
    print("new")
    r = session.get('http://paraiba.pb.gov.br/noticias?b_start:int='+str(i))
    links = r.html.find('a.summary.url')
    links = u.linkreturn(links)
    for j,link in enumerate(links):
        article = nw.Article(link)
        while True:
            print(j)
            print(link)
            try:
                time.sleep(timeout)
                article.download()
                article.parse()
            except nw.article.ArticleException:
                print("erro")
                timout = timeout+1
                retry = retry+1
                if retry == 3:
                    retry = 0
                    timeout = 2
                    break
                continue
            break
        with open(sys.argv[1],'a') as f:
            f.write(article.text)
    i = i+30
