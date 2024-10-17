import time

import pyautogui as pag


def is_present(img_path):
    return pag.locateOnScreen(img_path, confidence=0.9)


def wait_for_program(check_func):
    scan_frequency = 1.0
    time_start = time.time()

    is_present = check_func()
    while not is_present:
        time.sleep(scan_frequency - ((time.time() - time_start) % scan_frequency))
        is_present = check_func()


eastern_ready = "./screenshots/automatic_directory_creation/eastern_ready.png"

store_name = pag.prompt(text="", title="Enter store name!", default="")
time_zone = pag.prompt(
    text="",
    title="Eastern, Central, Mountain, Pacific, Alaskan, Hawaii, Puerto",
    default="Eastern",
)

print(store_name)
print(time_zone)

if time_zone == "Eastern":
    wait_for_program(lambda x=eastern_ready: is_present(x))
    pag.moveTo(483, 390)
if time_zone == "Central":
    wait_for_program(lambda x=eastern_ready: is_present(x))
    pag.moveTo(483, 423)
if time_zone == "Mountain":
    wait_for_program(lambda x=eastern_ready: is_present(x))
    pag.moveTo(481, 462)
if time_zone == "Pacific":
    wait_for_program(lambda x=eastern_ready: is_present(x))
    pag.moveTo(483, 497)
if time_zone == "Alaskan":
    wait_for_program(lambda x=eastern_ready: is_present(x))
    pag.moveTo(483, 536)
if time_zone == "Hawaii":
    wait_for_program(lambda x=eastern_ready: is_present(x))
    pag.moveTo(482, 572)
if time_zone == "Puerto":
    wait_for_program(lambda x=eastern_ready: is_present(x))
    pag.moveTo(481, 609)
