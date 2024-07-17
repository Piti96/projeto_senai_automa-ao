from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Edge()

driver.get("https://www.sp.senac.br/")
#Utilizando tempo
time.sleep(4)
driver.maximize_window()

barra_pesquisa = driver.find_element(By.ID,"mainBusca")

#clicando e preenchendo elemento

barra_pesquisa.send_keys("Administração")
time.sleep(5)

#Clicando na lupa de pesquisa
button_pesquisa = driver.find_element(By.XPATH, "lupa-busca")
button_pesquisa.click()


time.sleep(10)