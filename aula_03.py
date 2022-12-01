from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser = Chrome()

browser.get(url)

sleep(3)

a = browser.find_element(By.ID, 'ancora')
p = browser.find_element(By.TAG_NAME, 'p')

for click in range(10):
  txts = browser.find_elements(By.TAG_NAME, 'p')
  a.click()
  print(f'Valor do ultimo p: {txts[-1].text} - valor do click: {click} | equals? {int(txts[-1].text) == click}' )


## Exercicio 1 : https://curso-python-selenium.netlify.app/exercicio_01.html
dicionario = {
  'h1': {
    'p.atributo': 'conteudo',
    'p.atributo': 'conteudo',
    'p.atributo': 'conteudo'
  }
}
## Exercicio 2 : https://curso-python-selenium.netlify.app/exercicio_02.html


# print(f'texto de a: {a.text}')
# print(f'texto de p: {p.text}')


# Installed:
#  - selenium-chrome-driver v104.0.5112.79 (mod)
#  - selenium v3.141.59
#  - kb3033929 v1.0.5
#  - python3 v3.10.6
#  - selenium-gecko-driver v0.31.0
#  - chocolatey-windowsupdate.extension v1.0.4
#  - vcredist140 v14.32.31332
#  - kb2999226 v1.0.20181019
#  - selenium-edge-driver v6.17134.20180630
#  - kb2919355 v1.0.20160915
#  - chocolatey-core.extension v1.4.0
#  - selenium-all-drivers v4.0
#  - kb2919442 v1.0.20160915
#  - vcredist2015 v14.0.24215.20170201
#  - chocolatey-compatibility.extension v1.0.0
#  - selenium-ie-driver v3.150.1
#  - kb3035131 v1.0.3
#  - selenium-opera-driver v83.0.4103.97
#  - python v3.10.6