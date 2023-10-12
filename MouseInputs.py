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
        file.write('click_coordinates\n')
        file.write('show_commands\n')  # Added this line

def load_allowed_commands():
    with open('MouseCommands.txt', 'r') as file:
        commands = [line.strip() for line in file if line.strip()]
    return commands


# Ensure the text file is created first
create_text_file()

ALLOWED_COMMANDS = load_allowed_commands()

def process_twitch_message(message):
    # Check if the command is in the whitelist
    command = message.split()[0].lower()
    if command not in ALLOWED_COMMANDS:
        print(f"Command '{command}' is not allowed!")
        return

    # If the command is 'show_commands', display the list of valid commands
    if command == 'show_commands':
        show_valid_commands()
    else:
        # Execute the command
        MouseInputs(message)

def show_valid_commands(send_func):
    commands = []
    with open('MouseCommands.txt', 'r') as file:
        for line in file:
            cmd = line.strip()
            commands.append(cmd)
    
    # Join the command names into a single string and send
    send_func(', '.join(commands))


def MouseInputs(message, send_func):
    match = re.match(r'([a-z_]+)(\d+)?,?(\d+)?', message.lower())
    if not match:
        print("Invalid command")
        return

    command, arg1, arg2 = match.groups()

    match command:
        case 'move_up':
            moveMouse(0, -int(arg1) if arg1 else -100)
        case 'move_down':
            moveMouse(0, int(arg1) if arg1 else 100)
        case 'move_left':
            moveMouse(-int(arg1) if arg1 else -100, 0)
        case 'move_right':
            moveMouse(int(arg1) if arg1 else 100, 0)
        case 'click_left':
            clickMouse('left')
        case 'click_right':
            clickMouse('right')
        case 'scroll_up':
            scrollMouse(1)
        case 'scroll_down':
            scrollMouse(-1)
        case 'draw_circle':
            draw_circle(int(arg1) if arg1 else 100)
        case 'time':
            print(time.time())
        case 'click_coordinates':
            if arg1 and arg2:
                click_coordinates(int(arg1), int(arg2))
            else:
                print("Invalid coordinates")
        case 'show_commands':
            show_valid_commands(send_func)

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

def click_coordinates(x, y):
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()

def add_allowed_command(command):
    with open('MouseCommands.txt', 'a') as f:
        f.write(command + '\n')
