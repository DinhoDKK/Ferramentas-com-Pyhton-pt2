from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site esta recebendo o conteudo da requisição http do site..
soup = BeautifulSoup(site, 'html.parser')
#objeto soup esta baixando do site o html
#print(soup.prettify())
#tranformar o html em string e vai exibir o html

temperatura = soup.find("h6", class_="copyright")

print(temperatura.string)

print(soup.title.string)

print(soup.find('admin'))