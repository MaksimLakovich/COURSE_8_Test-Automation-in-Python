from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By


def setup_browser():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def open_store(browser, url):
    try:
        browser.get(url)
    except Exception as info:
        print("Ошибка при открытии страницы:", info)


def costumer_authorization(browser, by, search_input_user_name, search_input_user_password, user_name, user_password, search_button_login):
    try:
        browser.find_element(by, search_input_user_name).send_keys(user_name)
        browser.find_element(by, search_input_user_password).send_keys(user_password)
        browser.find_element(by, search_button_login).click()
    except WebDriverException as info:
        print("Ошибка при установке времени задержки:", info)
        browser.quit()
        raise


def add_product_to_cart(browser, by, search_sauce_labs_backpack, search_sauce_labs_bolt_t_shirt, search_sauce_labs_onesie):
    try:
        browser.find_element(by, search_sauce_labs_backpack).click()
        browser.find_element(by, search_sauce_labs_bolt_t_shirt).click()
        browser.find_element(by, search_sauce_labs_onesie).click()
    except WebDriverException as info:
        print("Ошибка добавления товара в корзину", info)
        browser.quit()
        raise


def go_cart_and_check_product(browser, by, search_cart_link, search_button_checkout):
    try:
        browser.find_element(by, search_cart_link).click()
        browser.find_element(by, search_button_checkout).click()
    except WebDriverException as info:
        print("Ошибка перехода и проверки корзины:", info)
        browser.quit()
        raise


def fill_user_form(browser, by, search_input_first_name, search_input_last_name, search_input_postal_code, first_name, last_name, postal_code, search_button_continue):
    try:
        browser.find_element(by, search_input_first_name).send_keys(first_name)
        browser.find_element(by, search_input_last_name).send_keys(last_name)
        browser.find_element(by, search_input_postal_code).send_keys(postal_code)
        browser.find_element(by, search_button_continue).click()
    except WebDriverException as info:
        print("Ошибка заполнения формы пользователя:", info)
        browser.quit()
        raise


def read_total_price(browser, by, search_total):
    try:
        total_price = browser.find_element(by, search_total).text
        print(total_price)
    except WebDriverException as info:
        print("Ошибка чтения итоговой суммы к оплате:", info)
        browser.quit()
        raise      


def test_for_online_store():
    browser = setup_browser()
    url = "https://www.saucedemo.com/"
    search_input_user_name = "#user-name"
    search_input_user_password = "#password"
    user_name = "standard_user"
    user_password = "secret_sauce"
    search_button_login = "#login-button"
    search_sauce_labs_backpack = "#add-to-cart-sauce-labs-backpack"
    search_sauce_labs_bolt_t_shirt = "#add-to-cart-sauce-labs-bolt-t-shirt"
    search_sauce_labs_onesie = "#add-to-cart-sauce-labs-onesie"
    search_cart_link = ".shopping_cart_link"
    search_button_checkout = "#checkout"
    search_input_first_name = "#first-name"
    search_input_last_name = "#last-name"
    search_input_postal_code = "#postal-code"
    first_name = "Иван"
    last_name = "Петров"
    postal_code = "230129"
    search_button_continue = "#continue"
    search_total = "#checkout_summary_container > div > div.summary_info > div.summary_total_label"

    try:
        open_store(browser, url)
        costumer_authorization(browser, By.CSS_SELECTOR, search_input_user_name, search_input_user_password, user_name, user_password, search_button_login)
        add_product_to_cart(browser, By.CSS_SELECTOR, search_sauce_labs_backpack, search_sauce_labs_bolt_t_shirt, search_sauce_labs_onesie)
        go_cart_and_check_product(browser, By.CSS_SELECTOR, search_cart_link, search_button_checkout)
        fill_user_form(browser, By.CSS_SELECTOR, search_input_first_name, search_input_last_name, search_input_postal_code, first_name, last_name, postal_code, search_button_continue)
        read_total_price(browser, By.CSS_SELECTOR, search_total)

        total_price = browser.find_element(By.CSS_SELECTOR, search_total)
        res = total_price.text
        test_result = res
        assert test_result == "Total: $58.29"
    
    finally:
        browser.quit()
