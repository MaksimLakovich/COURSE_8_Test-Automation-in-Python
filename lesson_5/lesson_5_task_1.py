"""Для инфо: по ходу выполнения следующих задач начал писать более корректный код с использованием конструкции 
   try/except(NoSuchElementException, WebDriverException)/finaly. А в последних заданиях с переходом на использование def().
   Исправлять первое задание уже не стал и оставил в просто виде, так как оно так же по факту является корректно работающим"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")                                             # зайти на сайт в Chrome
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")                                            # зайти на сайт в Firefox

define_button_add = "button"
define_button_delete = "button.added-manually"

for x in range(0, 5):                                                                                            # определить кнопку "Добавить" и нажать ее 5 раз
    add_elements_chrome = chrome.find_element(By.CSS_SELECTOR, define_button_add)
    add_elements_chrome.send_keys(Keys.RETURN)
    add_elements_firefox = firefox.find_element(By.CSS_SELECTOR, define_button_add)
    add_elements_firefox.send_keys(Keys.RETURN)

buttons_delete_chrome = chrome.find_elements(By.CSS_SELECTOR, define_button_delete)                              # посчитать количество кнопок "Delete" в браузерах
buttons_delete_firefox = firefox.find_elements(By.CSS_SELECTOR, define_button_delete)

print(f"Количество кнопок 'Delete' в браузере Chrome: {len(buttons_delete_chrome)}")
print(f"Количество кнопок 'Delete' в браузере Firefox: {len(buttons_delete_firefox)}")

sleep(3)

chrome.quit()
firefox.quit()
