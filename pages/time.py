from selenium.webdriver.common.by import By

from pages.base import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WaitTime(BasePage):
    def time_test(self, identificador):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, identificador)))