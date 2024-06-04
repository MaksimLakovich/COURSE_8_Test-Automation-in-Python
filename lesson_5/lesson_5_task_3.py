"""Для инфо: сайт каждый раз при открыти новой страницы браузера меняет местами кнопки (желтая, синяя, зеленая) и при этом 
   каждый раз меняется набор классов для них. Поэтому важно в тесте не просто 3 раза нажать на СИНЮЮ кнопку, а сделать это 
   в открывшихся 3-х разных страницах браузера. Только так будет проверено, что код корректно работает несмотря на рандомное отображение кнопок на странице."""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException


search_button_with_css_class = ".btn-primary"
count_push_blue_button_in_chrome = 0
count_push_blue_button_in_firefox = 0

for x in range(0, 3):

    try:
        chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        chrome.get("http://uitestingplayground.com/classattr")
        sleep(1)
        try:
            push_blue_button = chrome.find_element(By.CSS_SELECTOR, search_button_with_css_class).send_keys(Keys.RETURN)
            sleep(1)
            chrome.switch_to.alert.accept()
            sleep(1)
            print("Нажата синяя кнопка и закрыт alert в браузере Chrome")
        except NoSuchElementException:
            print("Такой элемент не найден на странице браузера Chrome")
        count_push_blue_button_in_chrome += 1
    except WebDriverException as info:
        print(f"Ошибка инициализации веб-драйвера Chrome: {info}")
    finally:
        chrome.quit()

    try:
        firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        firefox.get("http://uitestingplayground.com/classattr")
        sleep(1)
        try:
            push_blue_button = firefox.find_element(By.CSS_SELECTOR, search_button_with_css_class).send_keys(Keys.RETURN)
            sleep(1)
            firefox.switch_to.alert.accept()
            sleep(1)
            print("Нажата синяя кнопка и закрыт alert в браузере Firefox")
        except NoSuchElementException:
            print("Такой элемент не найден на странице браузера Firefox")
        count_push_blue_button_in_firefox += 1
    except WebDriverException as info:
        print(f"Ошибка инициализации веб-драйвера Chrome: {info}")
    finally:
        firefox.quit()

print("Количество итераций открытия страницы и нажатия синей кнопки в браузере Chrome:", count_push_blue_button_in_chrome)
print("Количество итераций открытия страницы и нажатия синей кнопки в браузере Firefox:", count_push_blue_button_in_firefox)
