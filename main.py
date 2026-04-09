import socket
import time
import pyautogui

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target_ip = "127.0.0.1"
port = 5005

while True:
    x, y = pyautogui.position()
    message = f"{x},{y}".encode()
    sock.sendto(message, (target_ip, port))
    time.sleep(0.01)
