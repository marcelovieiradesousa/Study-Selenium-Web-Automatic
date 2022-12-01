from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
driver.get(url)

sleep(3)

ancora = driver.find_element(By.TAG_NAME, "a")
p_num_esperado = driver.find_elements(By.TAG_NAME, "p")[1].text


separador_de_numero = slice(17, 19)
numero_esperado_inteiro = int(p_num_esperado[separador_de_numero])


ancora.click()
sleep(2)

tentativa = driver.find_elements(By.TAG_NAME, "p")[-1].text
won = "Você ganhou: " + str(numero_esperado_inteiro)

if won == tentativa:
  driver.quit()
while tentativa != won:
  ancora.click()
  tentativa = driver.find_elements(By.TAG_NAME, "p")[-1].text
  sleep(2)
  print(f'tentativa: {tentativa} | "won": {won}')
driver.quit()