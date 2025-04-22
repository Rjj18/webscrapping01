from bs4 import BeautifulSoup
import requests

url = "https://medium.com/editora-globo/testes-em-python-i-testando-requests-28c049805f41"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all("a")

print(len(links))