import pyautogui

def hkeys():
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    temp = pyautogui.confirm(text='quantas hotkeys tem seu pokemon?', title='BOT', buttons=keys)
    return temp


print(hkeys())