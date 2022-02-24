from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario, ):
    options = Options()
    options.add_argument("--no-sandbox")  # bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(executable_path=r"C:\Users\amay801549\.wdm\drivers\chromedriver\win32\98.0.4758"
                                                   #   r".102\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


def after_scenario(context, scenario):
    context.driver.close()
