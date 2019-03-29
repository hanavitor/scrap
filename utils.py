import re

def link_return(hlinks):
    links = []
    for i,link in enumerate(hlinks):
        #adiciona links encontrados no atributo href
        links.append(link.attrs['href'])
        if re.match("http",link.attrs['href']) == False:
            #remove hrefs que nao sao links
            link.pop()
        if i > 0 and links[-1] == links[-2]:
            #remove links repetidos
            links.pop()
    #retorna lista de links
    return links
