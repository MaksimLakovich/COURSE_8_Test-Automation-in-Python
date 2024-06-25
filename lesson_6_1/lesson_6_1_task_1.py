"""Пишу скрипт только для одного браузера (Chrome), но в реальном проекте добавлял бы в код инициализацию и других браузеров"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


# Инициализация веб-драйверов
def setup_browser():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Открытие веб-страницы и установка рекомендуемого неявного ожидания по умолчанию = 4 сек на прогрузку всех элементов
def open_page(browser, url):
    try:
        browser.get(url).implicitly_wait(4)
    except Exception as info:
        print("Ошибка при открытии страницы:", info)


# Поиск полей на форме и их заполнение тестовыми значениями
def fill_form(browser, by,
              input_first_name, input_last_name, input_address, input_zip_code, input_email, input_phone_number, input_city, input_country, input_job_position, input_company,
              value_first_name, value_last_name, value_address, value_zip_code, value_email, value_phone_number, value_city, value_country, value_job_position, value_company
              ):
    try:
        browser.find_element(by, input_first_name).send_keys(value_first_name)
        browser.find_element(by, input_last_name).send_keys(value_last_name)
        browser.find_element(by, input_address).send_keys(value_address)
        browser.find_element(by, input_zip_code).send_keys(value_zip_code)
        browser.find_element(by, input_email).send_keys(value_email)
        browser.find_element(by, input_phone_number).send_keys(value_phone_number)
        browser.find_element(by, input_city).send_keys(value_city)
        browser.find_element(by, input_country).send_keys(value_country)
        browser.find_element(by, input_job_position).send_keys(value_job_position)
        browser.find_element(by, input_company).send_keys(value_company)
    except WebDriverException as info:
        print("Ошибка при заполнении полей страницы:", info)
        browser.quit()
        raise


# Нажатие кнопки Submit
def press_button(browser, by, search_button_submit):
    try:
        browser.find_element(by, search_button_submit).click()
    except WebDriverException as info:
        print("Ошибка при нажатии кнопки:", info)
        browser.quit()
        raise


# Консолидация в единую тестовую функцию, которая проверяет, что:
#     1) что поле Zip-code подсвечено красным / background-color: "rgba(248, 215, 218, 1)"
#     2) что остальные поля подсвечены зеленым / background-color: "rgba(209, 231, 221, 1)"
def test_for_elements_color():
    browser = setup_browser()
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    input_first_name = "[name='first-name']"
    input_last_name = "[name='last-name']"
    input_address = "[name='address']"
    input_zip_code = "[name='zip-code']"
    input_email = "[name='e-mail']"
    input_phone_number = "[name='phone']"
    input_city = "[name='city']"
    input_country = "[name='country']"
    input_job_position = "[name='job-position']"
    input_company = "[name='company']"
    value_first_name = "Иван"
    value_last_name = "Петров"
    value_address = "Ленина, 55-3"
    value_zip_code = ""
    value_email = "test@skypro.com"
    value_phone_number = "+7985899998787"
    value_city = "Москва"
    value_country = "Россия"
    value_job_position = "QA"
    value_company = "SkyPro"
    search_button_submit = "button"
    try:
        open_page(browser, url)
        fill_form(browser, By.CSS_SELECTOR,
                  input_first_name, input_last_name, input_address, input_zip_code, input_email, input_phone_number, input_city, input_country, input_job_position, input_company,
                  value_first_name, value_last_name, value_address, value_zip_code, value_email, value_phone_number, value_city, value_country, value_job_position, value_company
                  )
        press_button(browser, By.CSS_SELECTOR, search_button_submit)

        zip_code_element = browser.find_element(By.CSS_SELECTOR, "#zip-code")
        color_zip_code = zip_code_element.value_of_css_property("background-color")
        test_res = color_zip_code
        assert test_res == "rgba(248, 215, 218, 1)"

        other_elements = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"]
        for element in other_elements:
            elements = browser.find_element(By.CSS_SELECTOR, element)
            color_element = elements.value_of_css_property("background-color")
            test_res = color_element
            assert test_res == "rgba(209, 231, 221, 1)"

    finally:
        browser.quit()
