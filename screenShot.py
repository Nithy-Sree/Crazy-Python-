# pip install PyAutoGUI

import pyautogui

# instance used to take screenshot using screenshot() class
screenshot = pyautogui.screenshot()

# saving the ss using save method of screenshot() class
screenshot.save("screen.png")
