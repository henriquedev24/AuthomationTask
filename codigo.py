import time
import pyautogui 
import pandas as pd


# Entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.PAUSE = 1
pyautogui.press('enter')

pyautogui.PAUSE = 0.5
# Fazer login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(715,408)
pyautogui.write('gabriel@email.com')
pyautogui.press('tab')
pyautogui.write('459841')
pyautogui.click(967, 582)

time.sleep(2)

# Importar base de dados
tabela = pd.read_csv('produtos.csv')
pyautogui.PAUSE = 0.5
print(tabela)

# Cadastrar 1 produto

linha = 0

for linha in tabela.index:

    pyautogui.click(705,292)
    codigo = tabela.loc[linha, 'código']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)
    time.sleep(1)




# Repetir processo de cadastro até acabar os produtos
