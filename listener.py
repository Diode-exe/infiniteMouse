import socket
import time
import pyautogui

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5005))

while True:
    data, addr = sock.recvfrom(1024)
    x, y = map(int, data.decode().split(","))
    print(f"Received mouse position: ({x}, {y})")
    pyautogui.moveTo(x, y)
    time.sleep(0.05)