from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from urllib.parse import unquote
from json import loads

driver = Chrome()
url = 'http://selenium.dunossauro.live/exercicio_04.html'
driver.get(url)
sleep(3)

# Web Elements
name = driver.find_element(By.ID, 'nome')
email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'senha')
phone = driver.find_element(By.ID, 'telefone')
btn = driver.find_element(By.ID, 'btn')

# Dic de valores para inserir
dic_valores = {
  'nome': 'Maite',
  'email': 'maite@gmail.com',
  'senha': '1013@24Lrg',
  'telefone': '3198765432'
}
# Inserindo valores nos campos cpm pausas de 1s
name.send_keys(dic_valores.get('nome'))
# sleep(1)
email.send_keys(dic_valores.get('email'))
# sleep(1)
password.send_keys(dic_valores.get('senha'))
# sleep(1)
phone.send_keys(dic_valores.get('telefone'))
# sleep(1)
btn.click()


# buscando resultado do textarea na pagina nova
result = driver.find_element(By.TAG_NAME, 'textarea').text
result_ajust = result.replace('\'', "\"")
dic_result = loads(result_ajust)


# buscando valores na query da url
url = driver.current_url
query = urlparse(url).query
query_split = query.split('&')
## remover o botão
query_split.pop()
## arruma o %40 como @ em email(1) e senha(2)
query_split[1] = unquote(query_split[1], 'utf-8')
query_split[2] = unquote(query_split[2], 'utf-8')
## ajeita a query_split para ser transformada em DICT
lista_nome = []
lista_email = []
lista_senha = []
lista_telefone = []

lista_nome = query_split[0].split('=')
lista_email = query_split[1].split('=')
lista_senha = query_split[2].split('=')
lista_telefone = query_split[3].split('=')
list_query = lista_nome + lista_email + lista_senha + lista_telefone

## transforma query_split de LIST para DICT
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

### Driver code
dic_query = Convert(list_query)

#FIM: Comparando se os valores inseridos são iguais aos da url
assert dic_valores == dic_result == dic_query