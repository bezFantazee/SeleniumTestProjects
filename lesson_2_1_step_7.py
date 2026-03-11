import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# функция, которая вычисляет значение функции, для проверки результата
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.ID, "treasure")
    # получение значения атрибута
    x = chest.get_attribute("valuex")
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # выбор нужного значения checkbox и radiobutton
    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox.click()
    radioButton = browser.find_element(By.ID, "robotsRule")
    radioButton.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
    