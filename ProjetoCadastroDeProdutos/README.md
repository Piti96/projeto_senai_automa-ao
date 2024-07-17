
# Automação de tarefas com Python

Aula 1 do Curso **Jornada Python** da **Hashtag Programação**

## Cenário:

Tenho uma base de dados de produtos, uma base de dados densa. E eu preciso cadastrar esses produtos no sistema 1 vez por semana.

E não é possível fazer esse cadastro na mão de uma maneira rápida e eficiente. Além de demorar muito para eu cadastrar todos os produtos na mão, pode ser que eu cometa erros de digitação e etc.

Então, o melhor é ter um processo automatizado para realizar esse cadastro, para agilizar e otimizar esse processo.

Essa automação vai acessar o sistema da empresa, fazer o login, e começar a cadastrar cada produto presente na base de dados.

Com esse passo a passo lógico junto do conhecimento técnico, é possível automatizar qualquer processo que eu queira.

- **Resumo:** Automatizar o processo de cadastro e preenchimento de produtos no sistema da empresa.

## Ok, por onde começar?

- Primeira coisa a ser feita em QUALQUER CÓDIGO... Escrever em português o passo a passo do meu projeto, do que deve ser feito.

**Com o passo a passo definido, é so eu traduzir ele para python...**

### Passo a passo:

Passo 1: entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)

Passo 2: Fazer login (Preencher qualquer email e senha, é um sistema somente para teste)

Passo 3: importar/abrir a base de dados

Passo 4: Cadastrar um produto

Passo 5: Repetir o processo de cadastro (passo 4) para todos os produtos

## Bibliotecas utilizadas:
- pyautogui (automação de tela, teclado e mouse)
- time (definição de tempo)

### Alguns comandos principais do Pyautogui:

- `pyautogui.click` - clicar com o mouse
- `pyatutogui.write` - escrever um texto
- `pyautogui.press` - apertar teclas do teclado
- `pyautogui.hotkey` - combinação de teclas (ctrl + c)
- `pyautogui.scroll` - Rolar a tela para cima ou para baixo

### Documentação pyaytogui:

[Link Documentação](https://www.google.com/url?q=https%3A%2F%2Fpyautogui.readthedocs.io%2Fen%2Flatest%2F)

### Caso eu queira ver uma lista com o nome de todas as teclas do teclado:

- `print(pyautogui.KEYBOARD_KEYS)`
