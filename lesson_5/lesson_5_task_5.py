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
        raise UnsupportedBrowserException(f"Uncorrect browser's name: {name_browser}")


def type_text_in_field(browser, url, search_field_input, first_text, second_text):                         # открытие URL и ввод/изменение текста
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 10)
        type_text = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_field_input)))
        type_text.send_keys(first_text, Keys.RETURN)
        sleep(2)                                                                                           # небольшая задержка, чтоб визуально успеть увидеть
        type_text.clear()
        type_text.send_keys(second_text, Keys.RETURN)
        sleep(2)                                                                                           # небольшая задержка, чтоб визуально успеть увидеть
    except Exception as info:
        print("Детальное описание проблемы:", info)
    finally:
        browser.quit()


url = "http://the-internet.herokuapp.com/inputs"
search_field_input = "input"
first_text = "1000"
second_text = "999"

try:
    chrome_browser = setup_browser("chrome")
    type_text_in_field(chrome_browser, url, search_field_input, first_text, second_text)
except UnsupportedBrowserException as info:
    print(info)

try:
    firefox_browser = setup_browser("firefox")
    type_text_in_field(firefox_browser, url, search_field_input, first_text, second_text)
except UnsupportedBrowserException as info:
    print(info)
