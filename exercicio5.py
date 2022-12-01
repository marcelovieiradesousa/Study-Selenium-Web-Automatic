from random import random, seed
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
import random

driver = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_05.html'

driver.get(url)

sleep(3)



def preencher_forms():
  ## Form a ser preenchido...ou nao
  form_fillable = driver.find_element(By.TAG_NAME, 'span').text

  while form_fillable != "... Mentira, você conseguiu terminar":

    ## Achar o formulário na pagina
    pesquisa = f"[class*='{form_fillable}']"
    form = driver.find_element(By.CSS_SELECTOR, pesquisa)
    class_form = form.get_attribute("class")

    ## Achar e Preencher os campos
    campo_nome = driver.find_element(By.CSS_SELECTOR, f'.{class_form} input[name="nome"]')
    campo_senha = driver.find_element(By.CSS_SELECTOR, f'.{class_form} input[name="senha"]')
    btn_enviar = driver.find_element(By.CSS_SELECTOR,  f'.{class_form} input[type="submit"]')

    nomes = ["apple", "banana", "cherry", "gamer", "calipso", "epaminondas", "Filipe", "Palak", "Thiago", "Jucabra", "Karol", "tupp", "tupperware", "Garen", "Lissandra"]
    random.shuffle(nomes)
    campo_nome.send_keys(f'{nomes[0]}')
    sleep(1)
    campo_senha.send_keys(f'{random.randint(0,9)}')
    sleep(1)
    btn_enviar.click()
    form_fillable = driver.find_element(By.TAG_NAME, 'span').text
    
preencher_forms()
driver.quit()