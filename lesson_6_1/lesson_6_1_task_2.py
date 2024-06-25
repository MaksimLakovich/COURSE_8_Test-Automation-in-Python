from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_browser():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def open_calculator(browser, url):
    try:
        browser.get(url)
    except Exception as info:
        print("Ошибка при открытии страницы:", info)


def change_delay(browser, by, search_delay, num_1, num_2):
    try:
        # специально использую для практики вариант с имитацией клавиатуры (класс Keys), так как в данном поле пользователь не смог бы мышкой набрать 45
        browser.find_element(by, search_delay).click()
        browser.find_element(by, search_delay).send_keys(Keys.BACKSPACE, num_1, num_2)
    except WebDriverException as info:
        print("Ошибка при установке времени задержки:", info)
        browser.quit()
        raise


def summarise (browser, by, search_seven, search_plus, search_eight, search_equal_sign, search_spinner, timeout=60):
    try:
        browser.find_element(by, search_seven).click()
        browser.find_element(by, search_plus).click()
        browser.find_element(by, search_eight).click()
        browser.find_element(by, search_equal_sign).click()
        wait = WebDriverWait(browser, timeout)
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, search_spinner)))
    except TimeoutException:
        print("Таймаут ожидания браузера, пока элемент станет невидимым истек")
        browser.quit()
        raise


def test_for_calculator():
    browser = setup_browser()
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    search_delay = "#delay"
    search_seven = "#calculator > div.keys > span:nth-child(1)"
    search_plus = "#calculator > div.keys > span:nth-child(4)"
    search_eight = "#calculator > div.keys > span:nth-child(2)"
    search_equal_sign = "#calculator > div.keys > span.btn.btn-outline-warning"
    search_spinner = "#spinner"
    search_screen_result = "#calculator > div.top > div"
    num_1 = Keys.NUMPAD4
    num_2 = Keys.NUMPAD5

    try:
        open_calculator(browser, url)
        change_delay(browser, By.CSS_SELECTOR, search_delay, num_1, num_2)
        summarise(browser, By.CSS_SELECTOR, search_seven, search_plus, search_eight, search_equal_sign, search_spinner)

        sum_result = browser.find_element(By.CSS_SELECTOR, search_screen_result)
        res = sum_result.text
        test_sum_result = res
        assert test_sum_result == "15"

    finally:
        browser.quit()
