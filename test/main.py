from bs4 import BeautifulSoup as bs
import requests

URL = 'https://shopper.com.br/'
LOGIN = 'login'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'origin': 'https://landing.shopper.com.br', 'referer': 'https://landing.shopper.com.br/'}

s = requests.Session()

crsf_token = s.get('URL').cookies

print(crsf_token)

login_payload = {
  'email': 'matheus@matheusgrandi.com.br',
  'senha': 'LdyA3#5m@Fjv63'
}