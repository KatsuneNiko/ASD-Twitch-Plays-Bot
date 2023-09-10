import pyautogui
import time

# Takes the user message as a parameter.
def MouseInputs(message):
    testMessage = message.lower()

    # Map keywords to mouse inputs
    if testMessage == 'move_up':
        moveMouse(0, -100)
    elif testMessage == 'move_down':
        moveMouse(0, 100)
    elif testMessage == 'move_left':
        moveMouse(-100, 0)
    elif testMessage == 'move_right':
        moveMouse(100, 0)
    elif testMessage == 'click_left':
        clickMouse('left')
    elif testMessage == 'click_right':
        clickMouse('right')
    elif testMessage == 'scroll_up':
        scrollMouse(1)
    elif testMessage == 'scroll_down':
        scrollMouse(-1)
    elif testMessage == 'time':
        print(time.time())

# Move the mouse by (dx, dy) pixels
def moveMouse(dx, dy):
    x, y = pyautogui.position()
    pyautogui.moveTo(x + dx, y + dy, duration=0.2)

# Click the mouse
def clickMouse(button):
    pyautogui.click(button=button)

# Scroll the mouse wheel
def scrollMouse(amount):
    pyautogui.scroll(amount)
