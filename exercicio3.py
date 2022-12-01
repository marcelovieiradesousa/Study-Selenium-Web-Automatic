from pprint import pprint
from traceback import print_tb
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
# Confesso que era pra ter usado o urlparse para resolver a 3, mas demorei tanto nas funções que dei uma roubada. Eu diria que meu prgrama tem uma boa intuição com links maluciosos hahahahah!

driver = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_03.html'
driver.get(url)
urlparseada = urlparse(driver.current_url)

sleep(3)

### Page 0 → 'Começar por aqui'
ancora_start = driver.find_element(By.CSS_SELECTOR, '[attr]')
ancora_start.click()
sleep(3)

### Page 1 → 'Escolher o contrario'
#função: extrair ancoras
def get_anchores(browser, element): # list
  driver = browser
  tag = driver.find_element(By.TAG_NAME, element)
  anchores = tag.find_elements(By.TAG_NAME, 'a')
  return anchores

#função: extrair links
# senão houvesse apenas 2 alternativas, essa função não serviria
def get_hrefs(elements):
  links = ['alternativa 1', 'alternativa 2']
  for n in range(2):
    links[n] = elements[n].get_attribute('href')
  return links

#função: não escolher o diabao do erro
def evitar_o_ruim(escolha): 
  cilada = 'https://curso-python-selenium.netlify.app/diabao.html'
  dic = escolha
  for alternativa in range(2):
    if dic[alternativa] != cilada:
      return dic[alternativa]


main_a = get_anchores(driver, 'main')
links = list()
links = get_hrefs(main_a)
escolha_segura1 = evitar_o_ruim(links)
sleep(2)
#resolução
driver.get(escolha_segura1)

sleep(2)
### Page 2 → 'Responder qual o título da pagina'
main_a = get_anchores(driver, 'main')
links = get_hrefs(main_a)
escolha_segura2 = evitar_o_ruim(links)
sleep(2)
#resolução
driver.get(escolha_segura2)

sleep(2)
### Page 3 → 'Responder qual o da URL da pagina'
main_a = get_anchores(driver, 'main')
print(main_a)
links = get_hrefs(main_a)
print(links)
escolha_segura3 = evitar_o_ruim(links)
print(escolha_segura3)
sleep(2)
#resolução
driver.get(escolha_segura3)
sleep(1)
driver.refresh()