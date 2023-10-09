import math
import time
import pyautogui
import re
import os

# Create text file with allowed commands
def create_text_file():
    with open('MouseCommands.txt', 'w') as file:
        file.write('move_up\n')
        file.write('move_down\n')
        file.write('move_left\n')
        file.write('move_right\n')
        file.write('click_left\n')
        file.write('click_right\n')
        file.write('scroll_up\n')
        file.write('scroll_down\n')
        file.write('draw_circle\n')
        file.write('time\n')

# Load allowed commands from MouseCommands.txt
def load_allowed_commands():
    with open('MouseCommands.txt', 'r') as file:
        return [line.strip() for line in file]

# Ensure the text file is created first
create_text_file()

ALLOWED_COMMANDS = load_allowed_commands()

def process_twitch_message(message):
    # Check if the command is in the whitelist
    command = message.split()[0].lower()
    if command not in ALLOWED_COMMANDS:
        print(f"Command '{command}' is not allowed!")
        return

    # Execute the command
    MouseInputs(message)

def MouseInputs(message):
    match = re.match(r'([a-z_]+)(\d+)?', message.lower())
    if not match:
        print("Invalid command")
        return

    command, distance_str = match.groups()
    distance = int(distance_str) if distance_str else 100

    match command:
        case 'move_up':
            moveMouse(0, -distance)
        case 'move_down':
            moveMouse(0, distance)
        case 'move_left':
            moveMouse(-distance, 0)
        case 'move_right':
            moveMouse(distance, 0)
        case 'click_left':
            clickMouse('left')
        case 'click_right':
            clickMouse('right')
        case 'scroll_up':
            scrollMouse(1)
        case 'scroll_down':
            scrollMouse(-1)
        case 'draw_circle':
            draw_circle(distance)
        case 'time':
            print(time.time())

def moveMouse(dx, dy):
    x, y = pyautogui.position()
    pyautogui.moveTo(x + dx, y + dy, duration=0.2)

def clickMouse(button):
    pyautogui.click(button=button)

def scrollMouse(amount):
    pyautogui.scroll(amount)

def draw_circle(radius, num_points=100):
    x_center, y_center = pyautogui.position()
    angle_increment = 2 * math.pi / num_points
    
    for i in range(num_points + 1):
        angle = i * angle_increment
        x = x_center + radius * math.cos(angle)
        y = y_center + radius * math.sin(angle)
        pyautogui.moveTo(x, y, duration=0.1)


