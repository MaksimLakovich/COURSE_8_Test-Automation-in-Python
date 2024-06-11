from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException, TimeoutException


"""ВАРИАНТ 1:
   С использованием явного (explicit) ожидания - WEB_DRIVER_WAIT().
   Корректный, но крайне простой. Без отработки каких-либо возможных исключений/ошибок"""

# chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# chrome.get("http://uitestingplayground.com/ajax")

# press_button_triggering_ajax_request = chrome.find_element(By.CSS_SELECTOR, "#ajaxButton")
# press_button_triggering_ajax_request.click()

# wait_receive_text = WebDriverWait(chrome, 30)
# wait_receive_text.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#content > p")))

# text_element = chrome.find_element(By.CSS_SELECTOR, "#content > p")
# txt = text_element.text

# print(f"Получен следующий текст на странице: {txt}")
# chrome.quit()



"""ВАРИАНТ 2:
   С использованиес неявного (implicit) ожидания - IMPLICITLY_WAIT():
   Корректный, так как мы знаем об условии в 15 сек, но крайне простой. Без отработки каких-либо возможных исключений/ошибок"""

# chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# chrome.get("http://uitestingplayground.com/ajax")

# press_button_triggering_ajax_request = chrome.find_element(By.CSS_SELECTOR, "#ajaxButton")
# press_button_triggering_ajax_request.click()

# chrome.implicitly_wait(20)

# text_element = chrome.find_element(By.CSS_SELECTOR, "#content > p")
# txt = text_element.text

# print(f"Получен следующий текст на странице: {txt}")
# chrome.quit()



"""ВАРИАНТ 3:
   Улучшенный вариант, технически более корретный код (обработки исключений + функции + конструкции try/except/finally):
   С использованием явного (explicit) ожидания - WEB_DRIVER_WAIT()"""

# Инициализация веб-драйвера
def setup_driver():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Открытие веб-страницы
def open_page(driver, url):
    try:
        driver.get(url)
    except Exception as info:
        print("Веб-страница не была открыта:", info)


# Поиск и нажатие на синюю кнопку 
def click_button(driver, by, button_triggering_ajax_request):
    try:
        driver.find_element(by, button_triggering_ajax_request).click()
    except WebDriverException as info:
        print("Кнопка не была нажата:", info)
        driver.quit()
        raise


# Ожидание текста на зеленой плашке (15 сек на сайте)
def wait_text(driver, by, receive_text, timeout=30):
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(expected_conditions.visibility_of_element_located((by, receive_text)))
    except TimeoutException:
        print("Таймаут ожидания, пока элемент станет видимым истек")
        driver.quit()
        raise


# Получение текста с появившегося элемента
def get_green_element(driver, by, receive_text):
    element = driver.find_element(by, receive_text)
    return element.text


# Консолидирую все в функции в единую
def main():
    driver = setup_driver()
    try:
        open_page(driver, url)
        click_button(driver, By.CSS_SELECTOR, button_triggering_ajax_request)
        wait_text(driver, By.CSS_SELECTOR, receive_text)
        text = get_green_element(driver, By.CSS_SELECTOR, receive_text)
        print(f"Получен следующий текст на странице: {text}")
    finally:
        driver.quit()


# Запуск
url = "http://uitestingplayground.com/ajax"
button_triggering_ajax_request = "#ajaxButton"
receive_text = "#content > p"
main()
