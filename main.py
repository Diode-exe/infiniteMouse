import pyautogui

def main():
    # Move the mouse to a specific position
    pyautogui.moveTo(100, 100, duration=1)

    # Click the mouse at the current position
    pyautogui.click()

    # Type some text
    pyautogui.typewrite("Hello, World!", interval=0.1)