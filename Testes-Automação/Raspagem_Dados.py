#importando as bbibliotecas

from selenium import webdriver
from selenium.webdriver.common.by import By

#Instanciando o navegador

driver = webdriver.Chrome()

#abrindo a página do Google

driver.get("http://www.google.com.br/")

caixa_Pesquisa = driver.find_element(By.NAME, "q")
caixa_Pesquisa.send_keys("Python web scraping")
caixa_Pesquisa.submit()

#Aguardando a página de resultados carregar

driver.implicitly_wait(10)

#Extraindo os titulos dos resultados da busca

results = driver.find_elements(By.CSS_SELECTOR,"h3")

for result in results:
    print(result.text)

driver.quit()