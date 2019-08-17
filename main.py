from functions import *
from time import sleep


def main(battler):
    from time import time
    time_init = time()
    hknum = hkeys()
    sleep(3)
    poke_catched = 0
    catch_fish_position = find_fish()
    centered_catch_fish_position = pyautogui.center(catch_fish_position)
    catch_battler_position = pyautogui.center(battler)
    color_battler = pyautogui.pixel(catch_battler_position.x, catch_battler_position.y)
    while(True):
        launch_rod = to_fish(centered_catch_fish_position)
        if(launch_rod):
            clicked = verify_fish(centered_catch_fish_position)
            while(clicked == False):
                clicked = verify_fish(centered_catch_fish_position)
            poke_catched += 1
            print(statistic(time_init, poke_catched))
            attack(catch_battler_position, int(hknum)) 
        if color_battler != pyautogui.pixel(catch_battler_position.x, catch_battler_position.y):
            pyautogui.alert(text='Battler perdido, reinicie o bot', title='BATTLER LOST', button='OK')
            quit()            

if init() == 'INICIAR':
    catch_battler_position = find_battler()
    if catch_battler_position == None:
        pyautogui.alert(text='Battler não encontrado\nAtive o batter e tente novamente', title='Battler 404', button='OK')
        quit()
    main(catch_battler_position)
else:
    quit()
