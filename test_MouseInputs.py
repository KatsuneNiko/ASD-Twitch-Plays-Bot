import sys
import pytest
from unittest.mock import patch, mock_open, MagicMock
sys.modules['pyautogui'] = MagicMock()
import MouseInputs

@pytest.fixture
def mock_file():
    with patch("builtins.open", new_callable=mock_open) as mock_file:
        yield mock_file

def test_create_text_file(mock_file):
    MouseInputs.create_text_file()
    mock_file.assert_called_once_with('MouseCommands.txt', 'w')

def test_process_twitch_message_invalid_command():
    with patch("builtins.print") as mock_print:
        MouseInputs.process_twitch_message("invalid_command")
        mock_print.assert_called_once_with("Command 'invalid_command' is not allowed!")

def test_process_twitch_message_valid_command():
    with patch("MouseInputs.MouseInputs") as mock_mouse_inputs:
        MouseInputs.process_twitch_message("move_up")
        mock_mouse_inputs.assert_called_once_with("move_up")


def test_moveMouse():
    with patch("MouseInputs.pyautogui") as mock_pyautogui:
        mock_pyautogui.position.return_value = (0, 0)
        MouseInputs.moveMouse(10, 20)
        mock_pyautogui.moveTo.assert_called_once_with(10, 20, duration=0.2)

def test_clickMouse():
    with patch("MouseInputs.pyautogui") as mock_pyautogui:
        MouseInputs.clickMouse('left')
        mock_pyautogui.click.assert_called_once_with(button='left')

def test_scrollMouse():
    with patch("MouseInputs.pyautogui") as mock_pyautogui:
        MouseInputs.scrollMouse(1)
        mock_pyautogui.scroll.assert_called_once_with(1)

def test_draw_circle():
    with patch("MouseInputs.pyautogui") as mock_pyautogui:
        mock_pyautogui.position.return_value = (0, 0)
        MouseInputs.draw_circle(100)
        assert mock_pyautogui.moveTo.call_count > 0

def test_click_coordinates():
    with patch("MouseInputs.pyautogui") as mock_pyautogui:
        MouseInputs.click_coordinates(100, 200)
        mock_pyautogui.moveTo.assert_called_once_with(100, 200, duration=0.2)
        mock_pyautogui.click.assert_called_once()

def test_add_allowed_command(mock_file):
    MouseInputs.add_allowed_command("new_command")
    mock_file.assert_called_once_with('MouseCommands.txt', 'a')
