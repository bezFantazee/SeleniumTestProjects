from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    #получаем все элементы по селектору
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    #проходимся по всем элементам и устанавливаем в них нужное значение
    for element in elements:
        element.send_keys("м")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
