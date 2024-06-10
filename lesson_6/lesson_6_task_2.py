from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


# Инициализация веб-драйвера
def setup_driver():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Открытие веб-страницы
def open_page(driver, url):
    try:
        driver.get(url)
    except Exception as info:
        print("Веб-страница не была открыта:", info)


# Поиск поля и ввод нового названия
def set_new_button_name(driver, by, search_input_field, set_new_name):
    try:
        input_field = driver.find_element(by, search_input_field)
        input_field.send_keys(set_new_name)
    except WebDriverException as info:
        print("Новый текст не был введен:", info)
        driver.quit()
        raise


# Нажатие синей кнопки
def press_blue_button(driver, by, search_button_that_should_change):
    try:
        press_button = driver.find_element(by, search_button_that_should_change)
        press_button.click()
    except WebDriverException as info:
        print("Синяя кнопка не нажата:", info)
        driver.quit()
        raise


# Получить новый параметр (название) синей кнопки
def get_button_name(driver, by, search_button_that_should_change):
    try:
        new_button_name = driver.find_element(by, search_button_that_should_change)
        return new_button_name.text
    except WebDriverException as info:
        print("Не удалось получить новое название кнопки:", info)
        driver.quit()
        raise


# Консолидирую все в функции в единую
def main():
    driver = setup_driver()
    try:
        open_page(driver, url)
        previous_button_name = driver.find_element(By.CSS_SELECTOR, search_button_that_should_change).text
        set_new_button_name(driver, By.CSS_SELECTOR, search_input_field, set_new_name)
        press_blue_button(driver, By.CSS_SELECTOR, search_button_that_should_change)
        new_button_name = get_button_name(driver, By.CSS_SELECTOR, search_button_that_should_change)
        print(f"Предыдущее название кнопки: {previous_button_name}")
        print(f"Новое название кнопки: {new_button_name}")
    finally:
        driver.quit()


# Запуск
url = "http://uitestingplayground.com/textinput"
search_input_field = "#newButtonName"
set_new_name = "SkyPro"
search_button_that_should_change = "#updatingButton"
main()
