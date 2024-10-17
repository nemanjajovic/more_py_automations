import time

import keyboard
import pyautogui as pag


# My custom algorithm to wait for picture to appear on the screen then proceed with script execution
def is_present(img_path):
    return pag.locateOnScreen(img_path, confidence=0.9)


def wait_for_program(check_func):
    scan_frequency = 1.0
    time_start = time.time()

    is_present = check_func()
    while not is_present:
        time.sleep(scan_frequency - ((time.time() - time_start) % scan_frequency))
        is_present = check_func()


cmc_ready = "./screenshots/check_ld_services/CMC_ready.png"
services_ready = "./screenshots/check_ld_services/services_ready.png"


def do_job():
    # get current mouse position and save it for later so after script finishes we can return to the starting position
    current_position = pag.position()
    wait_for_program(lambda x=cmc_ready: is_present(x))
    pag.moveTo(633, 109)
    time.sleep(0.5)
    pag.click()
    # Wait for services to load
    wait_for_program(lambda x=services_ready: is_present(x))
    # Move to random service and click
    pag.moveTo(895, 308)
    pag.click()
    time.sleep(0.5)
    # Type L to move to services that start with "L"
    pag.press("l")
    # Return to current mouse position
    pag.moveTo(current_position.x, current_position.y)


while True:
    time.sleep(0.1)
    if keyboard.is_pressed("alt+f2"):
        do_job()
