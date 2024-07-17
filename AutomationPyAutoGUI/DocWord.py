import pyautogui
import time

#abrindo word
pyautogui.press('win')
pyautogui.write('word')
pyautogui.press('enter')
time.sleep(5)

#criando um novo documento
#pressionar duas teclas juntas - hotkey
pyautogui.hotkey('ctrl','n' )
time.sleep(1)

#Inserindo texto no documento 
pyautogui.write('i am not ')
pyautogui.press ('enter')
pyautogui.write('I am love very much play soccer.')

#salva o documento

pyautogui.hotkey('ctrl', 'b')
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('down')
time.sleep(3)
pyautogui.press('down')
time.sleep(3)
pyautogui.press('down')
time.sleep(3)
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write(' nostalgia for football ')
pyautogui.press('enter')

