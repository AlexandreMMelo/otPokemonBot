import pyautogui
from time import sleep

def iniciar():
    msg = '''
    1-Para pescar, ponha a barra de pesca sobre a agua.
    2-Deixe apenas os pokemons selvagens visiveis.
    3-Abra o jogo e inicie o bot
    4-Apenas inicie o bot com o battler vasio'''
    temp = pyautogui.confirm(text=msg, title='BOT', buttons=['INICIAR', 'ABORTAR'])
    return temp


def find_fish():
    coordinates = pyautogui.locateOnScreen('fish.png')
    return coordinates


def attack(coordinates, f):
    hotkeys = ['f1','f2','f4','f4','f5','f6','f7','f8','f9','f10','f11','f12'] 
    pyautogui.moveTo(coordinates.x-73, coordinates.y+34)
    sleep(0.5)
    pyautogui.click()
    temp = pyautogui.pixelMatchesColor(coordinates.x-73, coordinates.y+34, (11, 17, 35), tolerance=10)
    while temp == False:
        for i in range(f):
            pyautogui.hotkey(hotkeys[i])
            if temp = pyautogui.pixelMatchesColor(coordinates.x-73, coordinates.y+34, (11, 17, 35), tolerance=10):
                return True


def to_fish(coordinates):
    pyautogui.hotkey('shift', 'f1')
    pyautogui.moveTo(coordinates.x+15, coordinates.y+15)
    sleep(0.5)
    pyautogui.click()
    return True


def verify_fish(position_list):
    rbg_color_catched_fish = (84,181,62) # Green
    catched = pyautogui.pixelMatchesColor(position_list.x, position_list.y, rbg_color_catched_fish, tolerance=10)
    if(catched):
        click_to_catch_fish(position_list)
        return True
    else: return False


def click_to_catch_fish(position_list):
    pyautogui.moveTo(x=position_list.x, y=position_list.y)
    sleep(0.5)
    pyautogui.click()
    return True

def find_battler():
    coordinates = pyautogui.locateOnScreen('charles.png')
    return coordinates


def hkeys():
    msg = 'quantos mov tem seu pokemon?'
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    temp = pyautogui.confirm(text=msg, title='BOT', buttons=keys)
    return temp