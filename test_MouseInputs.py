import unittest
from unittest.mock import patch, mock_open, MagicMock
import MouseInputs

class TestMouseCommands(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_create_text_file(self, mock_file):
        MouseInputs.create_text_file()
        mock_file.assert_called_once_with('MouseCommands.txt', 'w')

    @patch("builtins.open", new_callable=mock_open, read_data="move_up\nmove_down\n")
    def test_load_allowed_commands(self, mock_file):
        commands = MouseInputs.load_allowed_commands()
        self.assertEqual(commands, ['move_up', 'move_down'])

    def test_process_twitch_message_invalid_command(self):
        with patch("builtins.print") as mock_print:
            MouseInputs.process_twitch_message("invalid_command")
            mock_print.assert_called_once_with("Command 'invalid_command' is not allowed!")

    @patch("MouseInputs.MouseInputs")
    def test_process_twitch_message_valid_command(self, mock_mouse_inputs):
        MouseInputs.process_twitch_message("move_up")
        mock_mouse_inputs.assert_called_once_with("move_up")

    @patch("builtins.open", new_callable=mock_open, read_data="move_up\nmove_down\n")
    def test_show_valid_commands(self, mock_file):
        mock_send_func = MagicMock()
        MouseInputs.show_valid_commands(mock_send_func)
        mock_send_func.assert_called_once_with('move_up, move_down')

    @patch("MouseInputs.pyautogui")
    def test_moveMouse(self, mock_pyautogui):
        mock_pyautogui.position.return_value = (0, 0)  # Mocking the return value
        MouseInputs.moveMouse(10, 20)
        mock_pyautogui.moveTo.assert_called_once()


    @patch("MouseInputs.pyautogui")
    def test_clickMouse(self, mock_pyautogui):
        MouseInputs.clickMouse('left')
        mock_pyautogui.click.assert_called_once_with(button='left')

    @patch("MouseInputs.pyautogui")
    def test_scrollMouse(self, mock_pyautogui):
        MouseInputs.scrollMouse(1)
        mock_pyautogui.scroll.assert_called_once_with(1)

    @patch("MouseInputs.pyautogui")
    def test_draw_circle(self, mock_pyautogui):
        mock_pyautogui.position.return_value = (0, 0)  # Mocking the return value
        MouseInputs.draw_circle(100)
        self.assertTrue(mock_pyautogui.moveTo.call_count > 0)

    @patch("MouseInputs.pyautogui")
    def test_click_coordinates(self, mock_pyautogui):
        MouseInputs.click_coordinates(100, 200)
        mock_pyautogui.moveTo.assert_called_once_with(100, 200, duration=0.2)
        mock_pyautogui.click.assert_called_once()

    @patch("builtins.open", new_callable=mock_open)
    def test_add_allowed_command(self, mock_file):
        MouseInputs.add_allowed_command("new_command")
        mock_file.assert_called_once_with('MouseCommands.txt', 'a')

    # ... Add more tests for other functions ...

if __name__ == '__main__':
    unittest.main()
