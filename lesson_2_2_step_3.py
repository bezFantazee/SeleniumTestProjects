from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # получаем значение текста необходимых элементов
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text

    # рассчитываем сумму
    ans = int(x) + int(y)
    # в выдающем списке выбираем значение равное рассчитанной сумме
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(ans))

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
