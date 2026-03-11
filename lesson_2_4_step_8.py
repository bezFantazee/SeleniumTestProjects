from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

from selenium.webdriver.support.wait import WebDriverWait


# функция, которая вычисляет значение функции, для проверки результата
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 15)
    # ожидаем пока цена не станет равной 100$
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"),
            "$100"
        )
    )
    # по завершению ожидания жмем кнопку
    startButton = browser.find_element(By.CLASS_NAME, "btn")
    startButton.click()

    # ищем нужный элемент и вычисляем функцию
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
