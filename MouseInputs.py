import pyautogui
import time
import math


# Takes the user message as a parameter.
def MouseInputs(message):
    testMessage = message.lower()

    # Map keywords to mouse inputs
    match testMessage:
        case 'move_up':
            moveMouse(0, -100)
        case 'move_down':
            moveMouse(0, 100)
        case 'move_left':
            moveMouse(-100, 0)
        case 'move_right':
            moveMouse(100, 0)
        case 'click_left':
            clickMouse('left')
        case 'click_right':
            clickMouse('right')
        case 'scroll_up':
            scrollMouse(1)
        case 'scroll_down':
            scrollMouse(-1)
        # case 'draw_circle':
        #     draw_circle(100)
        case 'time':
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

# #Draw a circle with the mouse
#Sorry this is a dumb idea
# def draw_circle(radius, num_points=100):
#     # Get the current mouse position
#     x_center, y_center = pyautogui.position()
    
#     # Calculate the angle increment between each point
#     angle_increment = 2 * math.pi / num_points
    
#     # Pause for a moment before drawing
#     time.sleep(2)
    
#     for i in range(num_points + 1):
#         # Calculate the angle at this point
#         angle = i * angle_increment
        
#         # Calculate the x and y coordinates for this point
#         x = x_center + radius * math.cos(angle)
#         y = y_center + radius * math.sin(angle)
        
#         # Move the mouse to this position
#         pyautogui.moveTo(x, y, duration=0.1)

# # Draw a circle with a radius of 100 pixels
# draw_circle(100)
