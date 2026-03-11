import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем форму
    inputName = browser.find_element(By.NAME, "firstname")
    inputName.send_keys("name")
    inputLastName = browser.find_element(By.NAME, "lastname")
    inputLastName.send_keys("last name")
    inputEmail = browser.find_element(By.NAME, "email")
    inputEmail.send_keys("email")

    # загружаем файл на страницу для получения пути к файлу используем библиотеку os
    pinFile = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    pinFile.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
