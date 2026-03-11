import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# список ссылок для проверки
lessons = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

# функция для авторизации в stepic
def login_to_stepik(browser, login, password):
    # ждем появления кнопки "Войти" и кликаем по ней
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
    )
    login_button.click()

    time.sleep(5)

    # вводим логин и пароль в появившейся форме
    login_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_login_email"))
    )
    login_input.send_keys(login)

    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys(password)

    # нажимаем кнопку "Войти" в форме
    submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit_button.click()

    # ждем, пока исчезнет попап авторизации
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
    )
    time.sleep(1)
    print("Авторизация выполнена успешно.")


# функция для ввода и отправки ответа
def submit_answer(browser):
    # ждем появления поля для ответа
    answer_input = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )

    # проверяем, не заполнено ли поле
    current_value = answer_input.get_attribute("value")

    # если поле не пустое, ищем и нажимаем кнопку .again-btn
    if current_value and current_value.strip():
        print("Поле не пустое, ищем кнопку .again-btn...")
        try:
            # ищем кнопку "Решить снова"
            again_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn"))
            )
            again_button.click()
            print("Кнопка .again-btn нажата")

            # ждем, пока поле очистится
            time.sleep(1)

            # обновляем ссылку на поле (после сброса DOM может обновиться)
            answer_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
            )
        except:
            print("Кнопка .again-btn не найдена или не кликабельна")
            # если кнопки нет, пробуем очистить поле программно
            try:
                answer_input.clear()
            except:
                browser.execute_script("arguments[0].value = '';", answer_input)
    else:
        # поле пустое, просто очищаем для надежности
        try:
            answer_input.clear()
        except:
            browser.execute_script("arguments[0].value = '';", answer_input)

    # ждем, когда поле станет интерактивным
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )

    # вычисляем и вводим ответ
    answer = str(math.log(int(time.time())))

    try:
        answer_input.send_keys(answer)
    except:
        browser.execute_script(f"arguments[0].value = '{answer}';", answer_input)

    # нажимаем кнопку отправки
    submit_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    submit_btn.click()
    print("Ответ отправлен")


# функция для получения фидбека
def get_feedback_text(browser):
    # ждем, пока появится поле с результатом
    feedback_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    return feedback_element.text

#ОСНОВНОЙ ТЕСТ
@pytest.mark.parametrize("url", lessons)
def test_stepik_lessons(browser, url):
    # данные для авторизации
    login = "davydovaksenia529@yandex.com"
    password = "1595qtot"

    browser.get(url)

    # выполняем авторизацию (если она требуется)
    login_to_stepik(browser, login, password)

    time.sleep(3)

    # отправляем правильный ответ
    submit_answer(browser)
    time.sleep(3)

    # получаем текст фидбека
    feedback_text = get_feedback_text(browser)

    # проверяем, что фидбек равен "Correct!"
    assert feedback_text == "Correct!", f"Ожидался 'Correct!', но получен: '{feedback_text}'"


