from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_element_present(driver, *element):
    is_present = True
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(element))
    except Exception as e:
        print(f'Element {element} was not found with error {e}')
        is_present = False
    return is_present
