import socket
import time
import pyautogui

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5005))

MOVE_THRESHOLD = 3  # pixels; ignore tiny jitter
SLEEP_SEC = 0.05

while True:
    data, addr = sock.recvfrom(1024)
    raw = data.decode(errors="replace").strip()
    # debug raw data to help diagnose unexpected packets
    print(f"Raw packet from {addr}: {raw!r}")

    parts = raw.split(",")
    if len(parts) != 2:
        print("Malformed packet (expected 'x,y'), skipping")
        time.sleep(SLEEP_SEC)
        continue

    try:
        x = int(parts[0].strip())
        y = int(parts[1].strip())
    except ValueError:
        print("Could not parse integers from packet, skipping")
        time.sleep(SLEEP_SEC)
        continue

    # clamp coordinates to screen bounds
    screen_w, screen_h = pyautogui.size()
    x = max(0, min(x, screen_w - 1))
    y = max(0, min(y, screen_h - 1))

    cur_x, cur_y = pyautogui.position()
    dx = abs(x - cur_x)
    dy = abs(y - cur_y)

    # ignore very small movements to avoid fight/oscillation with other apps
    if dx <= MOVE_THRESHOLD and dy <= MOVE_THRESHOLD:
        # print(f"Ignoring small move: dx={dx}, dy={dy}")
        time.sleep(SLEEP_SEC)
        continue

    print(f"Received mouse position: ({x}, {y}) from {addr}")
    pyautogui.moveTo(x, y)
    time.sleep(SLEEP_SEC)