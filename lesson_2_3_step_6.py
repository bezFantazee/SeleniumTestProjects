from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# функция, которая вычисляет значение функции, для проверки результата
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    buttonStart = browser.find_element(By.CLASS_NAME, "btn")
    buttonStart.click()

    # переключаемся на новую страничку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # ищем нужный элемент и вычисляем функцию
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    