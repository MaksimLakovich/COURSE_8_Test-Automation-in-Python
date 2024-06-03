from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class UnsupportedBrowserException(Exception):                                                              # если проблема в одном браузере, второя работает и т.д.
    pass


def setup_browser(name_browser):                                                                           # инсталяция веб-драйверов для Chrome/Firefox
    if name_browser == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif name_browser == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise UnsupportedBrowserException(f"Некорреткное название браузера: {name_browser}")
    

def type_text_in_field(browser, url, search_user_name, search_user_password, search_button_login, user_name, user_password):
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_user_name))).send_keys(user_name)
        sleep(1)                                                                                                               # чтоб визуально успеть увидеть
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_user_password))).send_keys(user_password)
        sleep(1)                                                                                                               # чтоб визуально успеть увидеть
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_button_login))).send_keys(Keys. RETURN)
        sleep(2)                                                                                                               # чтоб визуально успеть увидеть
    except Exception as info:
        print("Детальное описание проблемы:", info)
    finally:
        browser.quit()


url = "http://the-internet.herokuapp.com/login"
search_user_name = "#username"
search_user_password = "#password"
search_button_login = "button"
user_name = "tomsmith"
user_password = "SuperSecretPassword!"

try:
    chrome_browser = setup_browser("chrome")
    type_text_in_field(chrome_browser, url, search_user_name, search_user_password, search_button_login, user_name, user_password)
except UnsupportedBrowserException as info:
    print(info)

try:
    firefox_browser = setup_browser("firefox")
    type_text_in_field(firefox_browser, url, search_user_name, search_user_password, search_button_login, user_name, user_password)
except UnsupportedBrowserException as info:
    print(info)
