import pyautogui
import time

# Passo 1 - Entrar no sistema
pyautogui.PAUSE = 1.0 # Definindo um tempo para cada execução de comando, para que o pc tenha tempo de reconhecer cada comando

# Abrir o navegador 9 Apertar o botão windows e pesquisar pelo Edge)

pyautogui.press('win') # Botão do windows
pyautogui.write('edge') # Digitar edge
pyautogui.press('enter') # Pressionar enter

# Entrar no link do sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') # Digitar ma barra de pesquisa
pyautogui.press('enter') # Pressionar enter

# Usando time.sleep para esperar 3 segundos até o carregamento completo do site
time.sleep(3)

# Passo 2 - fazer login no sistema

pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'a') # Tratando para enviar caso esteja preenchendo automaticamente
time.sleep(3)
pyautogui.write('teste@hotmail.com') #Digitar o email
time.sleep(2)

# Para pular para o campo de senha utilizaremos o TAB, mas podemos tambem clicar utilizando as coordenadas
pyautogui.press('tab')
pyautogui.write('4789')
time.sleep(2)

# Clicar no botão
pyautogui.click(x=950, y=533)
time.sleep(2)

#Passo 3 - importar a base de dados
import pandas as pd 

produtos = pd.read_csv("produtos.csv") # variavel para ler dados

#3 passo 4 -  cadastrar produtos

for linha in produtos.index: # para cada linha dentro da tabela
    #codigo
    pyautogui.click(x=863, y=238)
    codigo = str(produtos.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca
    pyautogui.press('tab')
    marca = str(produtos.loc[linha, "marca"])
    pyautogui.write(marca) 

    #tipo
    pyautogui.press('tab')
    tipo = str(produtos.loc[linha, "tipo"])
    pyautogui.write(tipo)

    #categoria
    pyautogui.press('tab')
    categoria = str(produtos.loc[linha, "categoria"])
    pyautogui.write(categoria)

    #preco unitario
    pyautogui.press('tab')
    preco = str(produtos.loc[linha, "preco_unitario"])
    pyautogui.write(preco)

    #custo
    pyautogui.press('tab')
    custo = str(produtos.loc[linha, "custo"])
    pyautogui.write(custo)

    #obs
    pyautogui.press('tab')
    obs = str(produtos.loc[linha, "obs"])

    # Para tratar linhas nulas(nan) em obs
    if obs != "nan":
       pyautogui.write(obs)
    else:
       pyautogui.write("Sem observação")

    # Enviar
       
    pyautogui.press('tab')
    pyautogui.press('enter')

# scroll para subir a pagina ao topo
pyautogui.scroll(5000)






