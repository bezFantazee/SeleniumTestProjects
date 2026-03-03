#№1 1.6
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#    time.sleep(30)
#    # закрываем браузер после всех манипуляций
#    browser.quit()
#
# # не забываем оставить пустую строку в конце файла
import os
import re

#№2
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     link.click()
#
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()

#№3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.CSS_SELECTOR, "input")
#     for element in elements:
#         element.send_keys("м")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

#№4
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
#     elements = browser.find_elements(By.CSS_SELECTOR, "input")
#     for element in elements:
#         element.send_keys("м")
#
#     button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

#№5
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "https://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class input')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class input')
#     input3.send_keys("gmail@.gmail.com")
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#####2.1
#1
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     print(x)
#     y = calc(x)
#     print(y)
#     input = browser.find_element(By.ID, "answer")
#     input.send_keys(y)
#
#     checkBox = browser.find_element(By.ID, "robotCheckbox")
#     checkBox.click()
#     radioButton = browser.find_element(By.ID, "robotsRule")
#     radioButton.click()
#
#     button = browser.find_element(By.CLASS_NAME, "btn")
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()

#2
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     chest = browser.find_element(By.ID, "treasure")
#     x = chest.get_attribute("valuex")
#     y = calc(x)
#     input = browser.find_element(By.ID, "answer")
#     input.send_keys(y)
#
    # checkBox = browser.find_element(By.ID, "robotCheckbox")
    # checkBox.click()
    # radioButton = browser.find_element(By.ID, "robotsRule")
    # radioButton.click()
    #
    # button = browser.find_element(By.CLASS_NAME, "btn")
    # button.click()
# finally:
#     time.sleep(10)
#     browser.quit()

#3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# from selenium.webdriver.support.select import Select
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x = browser.find_element(By.ID, "num1").text
#     y = browser.find_element(By.ID, "num2").text
#     print(x, y)
#
#     ans = int(x) + int(y)
#     print(ans)
#     select = Select(browser.find_element(By.ID, "dropdown"))
#     select.select_by_value(str(ans))
#
#     button = browser.find_element(By.CLASS_NAME, "btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

#4
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x = browser.find_element(By.ID, "input_value").text
#     y = calc(x)
#
#     input = browser.find_element(By.ID, "answer")
#     checkBox = browser.find_element(By.ID, "robotCheckbox")
#     radioButton = browser.find_element(By.ID, "robotsRule")
#     button = browser.find_element(By.CLASS_NAME, "btn")
#
#     input.send_keys(y)
#     checkBox.click()
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     browser.execute_script("arguments[0].click();", radioButton)
#
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

#5
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     inputName = browser.find_element(By.NAME, "firstname")
#     inputName.send_keys("name")
#     inputLastName = browser.find_element(By.NAME, "lastname")
#     inputLastName.send_keys("last name")
#     inputEmail = browser.find_element(By.NAME, "email")
#     inputEmail.send_keys("email")
#
#     pinFile = browser.find_element(By.ID, "file")
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'file.txt')
#
#     pinFile.send_keys(file_path)
#
#     button = browser.find_element(By.CLASS_NAME, "btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

####2.3
#1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     buttonStart = browser.find_element(By.CLASS_NAME, "btn")
#     buttonStart.click()
#     alert = browser.switch_to.alert
#     alert.accept()
#
#     x = browser.find_element(By.ID, "input_value").text
#     y = calc(x)
#     input = browser.find_element(By.ID, "answer")
#     input.send_keys(y)
#
#     button = browser.find_element(By.CLASS_NAME, "btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

#2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     buttonStart = browser.find_element(By.CLASS_NAME, "btn")
#     buttonStart.click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x = browser.find_element(By.ID, "input_value").text
#     y = calc(x)
#     input = browser.find_element(By.ID, "answer")
#     input.send_keys(y)
#
#     button = browser.find_element(By.CLASS_NAME, "btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

#######2.4
#1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 15)
    #ожидаем пока цена не станет равной 100$
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"),
            "$100"
        )
    )

    startButton = browser.find_element(By.CLASS_NAME, "btn")
    startButton.click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()