import time
import random
from selenium.webdriver.common.action_chains import ActionChains

def human_like_typing(element, text):
    """
    Types the given text into the web element character by character
    with a random delay to mimic human behavior.

    :param element: The selenium web element (e.g., a text input field).
    :param text: The string to type.
    """
    for char in text:
        element.send_keys(char)
        # Introduce a random delay between 0.05 and 0.1 seconds
        time.sleep(random.uniform(0.05, 0.2))

def rand_delay():
    return .5 * random.uniform(0.7, 2)

def move_nat(driver, target):
    size = target.size
    click_x = int(size["width"] * random.uniform(0.3, 0.7))
    click_y = int(size["height"] * random.uniform(0.3, 0.7))

    # Move to element first
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(target, 0, 0)  # top-left of element

    # Gradually move to random click point
    steps = 10
    dx = click_x / steps
    dy = click_y / steps

    for i in range(steps):
        actions.move_by_offset(dx, dy)
        actions.pause(0.01 * random.uniform(0.7, 1.3))

    # Click
    # actions.click()
    actions.perform()
