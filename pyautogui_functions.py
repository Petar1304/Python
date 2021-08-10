import pyautogui
import os

width, height = pyautogui.size()

# pyautogui.moveTo(100, 500, duration=0.25)
# pyautogui.click(100, 100)
# pyautogui.scroll(200)
# im = pyautogui.screenshot()
# pyautogui.typewrite('Hello world!')

pyautogui.keyDown('shift')
# pyautogui.keyDown('S')
# pyautogui.keyUp('S')
pyautogui.press('s')
pyautogui.keyUp('shift')

