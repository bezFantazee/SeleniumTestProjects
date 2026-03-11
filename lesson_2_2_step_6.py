from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# функция, которая вычисляет значение функции, для проверки результата
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем нужный элемент и считаем значение функции
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # ищем элементы, которые необходимо заполнить
    input = browser.find_element(By.ID, "answer")
    checkBox = browser.find_element(By.ID, "robotCheckbox")
    radioButton = browser.find_element(By.ID, "robotsRule")
    button = browser.find_element(By.CLASS_NAME, "btn")

    input.send_keys(y)
    checkBox.click()
    # скролим страницу вниз и выбираем нужную radiobutton
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("arguments[0].click();", radioButton)

    button.click()

finally:
    time.sleep(10)
    browser.quit()
