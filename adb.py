import  os
import win32api
import keyboard
import pyauto
import time

toggle_n = 'n'
toggle_m = 'm'
toggle_button = '`'
toggle_c = 'c'
toggle_space = 'SPACE'
toggle_r = 'r'
toggle_f = 'f'
toggle_h = 'h'
toggle_t = 't'
toggle_v = 'v'
toggle_CTRL = 'CTRL'
toggle_TAB = 'TAB'
toggle_q = 'q'
toggle_e = 'e'
toggle_1 = '1'
toggle_2 = '2'
toggle_3 = '3'
toggle_4 = '4'
toggle_g = 'g'
toggle_b = 'b'
toggle_o = 'o'
toggle_p = 'p'
enabled = True


def midder():
    x, y = pyautogui.position()
    pyautogui.mouseDown(button='left')
    time.sleep(3)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(1050, 360)

    if x < 600 or x > 1450:
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(1050, 360)

    if y < 150 or y > 600:
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(1050, 360)


def is_mouse_down():    # Returns true if the left mouse button is pressed
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0
while True:
    if is_mouse_down() and enabled:#1280 560
        os.system("adb shell input tap 1280 560")

    key_c = keyboard.is_pressed(toggle_c)
    if key_c == True:
        os.system("adb shell input tap 1280 670")

    key_c = keyboard.is_pressed(toggle_c)
    if key_c == True:
        os.system("adb shell input tap 1280 670")#蹲

    key_v = keyboard.is_pressed(toggle_v)
    if key_v == True:
        os.system("adb shell input tap 1366 678")#伏

    key_space = keyboard.is_pressed(toggle_space)
    if key_space == True:
        os.system("adb shell input tap 1400 495")#跳

    key_r = keyboard.is_pressed(toggle_r)
    if key_r == True:
        os.system("adb shell input tap 1152 673")

    key_TAB = keyboard.is_pressed(toggle_TAB)
    if key_TAB== True:
        os.system("adb shell input tap 146 681")

    key_q = keyboard.is_pressed(toggle_q)
    if key_q == True:
        os.system("adb shell input tap 270 277")

    key_e = keyboard.is_pressed(toggle_e)
    if key_e == True:
        os.system("adb shell input tap 365 271")

    key_CTRL = keyboard.is_pressed(toggle_CTRL)
    if key_CTRL == True:
        os.system("adb shell input tap 1419 383")

    key_h = keyboard.is_pressed(toggle_h)
    if key_h == True:
        os.system("adb shell input tap 765 434")
    key_t = keyboard.is_pressed(toggle_t)
    if key_t == True:
        os.system("adb shell input tap 1102 186")
