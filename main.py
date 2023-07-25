import pygetwindow as gw
import pyautogui
import time
import random
import string

iteration_count = 1

for i in range(4):

    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    chrome_window.activate()

    time.sleep(3)   

    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite('www.facebook.com/ ')
    pyautogui.press('enter')        

    time.sleep(5)

    pyautogui.press('p')
    time.sleep(3)

    pyautogui.typewrite('https://www.facebook.com/sophisticatedgracephotography/posts/pfbid0bCrVrS2ndfnVA3nSmD1h56wL1xPW3Ae9gpFk7dfDsUVM3rSURVjtVCyNYcVAWiWQl')
    time.sleep(10)

    for _ in range(12):
        time.sleep(0.5)
        pyautogui.press('tab')

    pyautogui.press('enter')    

    time.sleep(5)

    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite('www.facebook.com/me')
    pyautogui.press('enter') 

    time.sleep(5)   

    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite('soph')

    for _ in range(3):
        time.sleep(0)                           
        pyautogui.press('tab')

    pyautogui.press('enter')    

    for _ in range(3):  
        pyautogui.hotkey('shift', 'tab')

    
    pyautogui.press('enter') 
    # pyautogui.press('enter') 
    
    time.sleep(2)
    pyautogui.press('c')
    time.sleep(1)
    
    for _ in range(2):
        alphanumeric = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        pyautogui.typewrite(alphanumeric)
        time.sleep(1)
        pyautogui.press('enter')

    time.sleep(3)    
    pyautogui.hotkey('ctrl', 'shift', 'm')
    time.sleep(1)    
    
    if iteration_count > 1:
        for _ in range(iteration_count - 1):
            pyautogui.press('down')
            time.sleep(1)    

    pyautogui.press('enter') 

    iteration_count += 1

    time.sleep(1)    