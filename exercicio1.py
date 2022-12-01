from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

driver.get(url)

sleep(3)
titulo = driver.find_element(By.TAG_NAME, "h1").text
chave1 = driver.find_element(By.CSS_SELECTOR, '[atributo=texto1]').get_attribute("atributo")
valor1 = driver.find_elements(By.TAG_NAME, "p")[0].text
chave2 = driver.find_element(By.CSS_SELECTOR, '[atributo=texto2]').get_attribute("atributo")
valor2 = driver.find_elements(By.TAG_NAME, "p")[1].text
chave3 = driver.find_element(By.CSS_SELECTOR, '[atributo=texto3]').get_attribute("atributo")
valor3 = driver.find_elements(By.TAG_NAME, "p")[2].text


dicionario = {
  titulo : {
    chave1: valor1,
    chave2: valor2,
    chave3: valor3
  }
}

print(dicionario)


driver.quit()