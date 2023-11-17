import requests
from bs4 import BeautifulSoup
url='https://tribunademinas.com.br/noticias/cultura'
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content,'html.parser')
    m=[]
    div_noticias = soup.find_all('div',class_='col-sm-12')

    for div_noticia in div_noticias:
        h2 = div_noticia.find('h2')
        if h2:
            print(h2.text)
else:
    print("Falha na requisição: Status Code", response.status_code)
