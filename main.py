import cv2
import time
import autopy
import keyboard
import threading
import numpy as np

from mss import mss
from PIL import Image
from collections import namedtuple

Point = namedtuple("Point", "x y")


# SCRIPT CFG

left = Point(x=621, y=333)
right = Point(x=742, y=333)

monitor = {
    'top': 0,
    'left': 0,
    'width': 1366,
    'height': 768
}

started: bool = False
mss_obj = mss()

INTERVAL = 0.059  # 59 ms
RANGE = 130  # 130 pixels

# END SCRIPT CFG


def screenshot_cv2():
    screen = mss_obj.grab(monitor)
    img = np.array(Image.frombytes('RGB', (screen.width, screen.height), screen.rgb))
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


def set_left():
    global left
    left = autopy.mouse.location()
    left = Point(x=left[0], y=left[1])
    print("left: ", left)


def set_right():
    global right
    right = autopy.mouse.location()
    right = Point(x=right[0], y=right[1])
    print("right: ", right)


def start():
    last_key = autopy.key.Code.LEFT_ARROW

    while True:

        if not started:
            return

        screenshot = screenshot_cv2()

        for color in screenshot[left.y - RANGE:left.y, left.x]:

            if tuple(color)[::-1] in ((161, 116, 56), (136, 99, 50)):
                last_key = autopy.key.Code.RIGHT_ARROW
                autopy.key.tap(last_key)
                break
        else:
            for color in screenshot[right.y - RANGE:right.y, right.x]:
                if tuple(color)[::-1] in ((161, 116, 56), (136, 99, 50)):
                    last_key = autopy.key.Code.LEFT_ARROW
                    autopy.key.tap(last_key)
                    break
            else:
                autopy.key.tap(last_key)

        time.sleep(INTERVAL)


def toggle_start():
    global started

    if right is None or left is None:
        print("no pos")
        return

    if not started:
        started = True
        thread = threading.Thread(target=start)
        thread.start()
    else:
        started = False


def start_script():
    keyboard.add_hotkey('ctrl + 1', set_left)
    keyboard.add_hotkey('ctrl + 2', set_right)
    keyboard.add_hotkey('ctrl + 3', toggle_start)
    keyboard.wait('esc')


if __name__ == '__main__':
    start_script()

