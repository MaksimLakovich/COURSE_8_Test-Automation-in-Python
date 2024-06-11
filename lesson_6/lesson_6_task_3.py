"""В реальном проекте по этой задаче писал бы код с использованием def.
   Т.е. по примеру предыдущих двух задач домашней работы (lesson_task_2 и lesson_task_3)"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    # Запуск Chrome
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидание появления текста "Done!" в элементе с локатором "#text"
    wait = WebDriverWait(chrome, 30)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!"))
    
    # Получение и вывод значения атрибута src у 3-й картинки
    element = chrome.find_element(By.CSS_SELECTOR, "#award")
    src_value = element.get_attribute("src")
    print(f"Получено следующее значение атрибута src у 3-й картинки: {src_value}")

except Exception as info:
        print("Произошла ошибка:", info)

# Закрытие браузера
finally:
    if 'chrome' in locals():
        chrome.quit()
