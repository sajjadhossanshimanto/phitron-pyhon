import pyautogui
from time import sleep


n = int(input())

sleep(2)
for i in range(n):
    # print("#"*(i+1))
    pyautogui.write("#"*(i+1), interval=.25)
    pyautogui.press("enter")
