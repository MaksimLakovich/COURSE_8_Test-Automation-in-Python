"""Для инфо: сайт каждый раз при открыти новой страницы браузера генирирует для кнопки "button_with_dynamic_id" новый ID-кнопки.
   Поэтому важно в тесте не просто 3 раза нажать на кнопку, а сделать это в открывшихся 3-х разных страницах браузера.
   Только так будет проверено, что код корректно работает не смотря на генерацию новых ID-кнопки."""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException


search_button_with_dynamic_id = ".btn.btn-primary"
count_open_and_push_button_in_chrome = 0
count_open_and_push_button_in_firefox = 0

for x in range(0, 3):

    try:
        chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        chrome.get("http://uitestingplayground.com/dynamicid")                                                   # зайти на сайт
        sleep(1)                                                                                                 # задержка чтоб увидеть, что кнопка еще не нажата
        try:                                                                                                     # определить кнопку "Добавить" и нажать её
            push_button_chrome = chrome.find_element(By.CSS_SELECTOR, search_button_with_dynamic_id).send_keys(Keys.RETURN)
            sleep(1)                                                                                             # задержка чтоб увидеть факт нажатия кнопки
        except NoSuchElementException:                                                                           # обрабатывает ошибки, если элемент не найден
            print("Такой элемент не найден на странице браузера Chrome")
        count_open_and_push_button_in_chrome += 1
    except WebDriverException as info:                                                                           # обрабатывает ошибки, если проблемы с веб-драйвером
        print(f"Ошибка инициализации веб-драйвера Chrome: {info}")                                               # в INFO записываю и вывожу описание ошибки
    finally:
        chrome.quit()                                                                                            # закрытие браузера после каждой итерации

    try:
        firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        firefox.get("http://uitestingplayground.com/dynamicid")
        sleep(1)
        try:
            push_button_firefox = firefox.find_element(By.CSS_SELECTOR, search_button_with_dynamic_id).send_keys(Keys.RETURN)
            sleep(1)
        except NoSuchElementException:
            print("Такой элемент не найден на странице браузера Firefox")
        count_open_and_push_button_in_firefox += 1
    except WebDriverException as info:
        print(f"Ошибка инициализации веб-драйвера Firefox: {info}")
    finally:
        firefox.quit()

print("Финальный подсчет количества итераций открытия страницы в браузере Chrome:", count_open_and_push_button_in_chrome)
print("Финальный подсчет количества итераций открытия страницы в браузере Firefox:", count_open_and_push_button_in_firefox)
