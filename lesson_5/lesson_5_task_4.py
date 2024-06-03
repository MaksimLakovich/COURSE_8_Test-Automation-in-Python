"""Вариант №1: примитивный"""
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# search_close_button_selector = ".modal-footer"
# chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# chrome.get("http://the-internet.herokuapp.com/entry_ad")
# sleep(3)                                                                                        # задержка чтоб дождаться появления модального окна (вместо wait)
# close_button = chrome.find_element(By.CSS_SELECTOR, search_close_button_selector)
# close_button.click()
# chrome.quit()


"""Вариант №2: технически более корректный и надежный"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UnsupportedBrowserException(Exception):                                                              # если проблема в одном браузере, второя работает и т.д.
    pass

def setup_browser(browser_name):                                                                           # инсталяция веб-драйверов для Chrome и Firefox
    if browser_name == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise UnsupportedBrowserException(f"Имя браузера определено некорректно: {browser_name}")

def open_page_and_close_modal(browser, url, search_close_button_selector):                                 # открытие URL и закрытие модального окна
    try:
        browser.get(url)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
        close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_close_button_selector)))
        close_button.click()
    except Exception as info:
        print("Детальное описание проблемы:", info)
    finally:
        browser.quit()

url = "https://the-internet.herokuapp.com/entry_ad"
search_close_button_selector = ".modal-footer"

try:
    chrome_browser = setup_browser("chrome")                                                               # запуск для Chrome
    open_page_and_close_modal(chrome_browser, url, search_close_button_selector)
except UnsupportedBrowserException as info:
    print(info)

try:
    firefox_browser = setup_browser("firefox")                                                             # запуск для Firefox
    open_page_and_close_modal(firefox_browser, url, search_close_button_selector)
except UnsupportedBrowserException as info:
    print(info)
