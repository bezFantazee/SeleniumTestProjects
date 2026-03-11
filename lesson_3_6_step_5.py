import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- СПИСОК УРОКОВ ДЛЯ ПРОВЕРКИ ---
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

def login_to_stepik(browser, login, password):
    # Ждем появления кнопки "Войти" и кликаем по ней
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
    )
    login_button.click()

    time.sleep(5)

    # Вводим логин и пароль в появившейся форме
    login_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_login_email"))
    )
    login_input.send_keys(login)

    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys(password)

    # Нажимаем кнопку "Войти" в форме
    submit_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit_button.click()

    # Ждем, пока исчезнет попап авторизации (или появится аватарка пользователя)
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
    )
    time.sleep(1)
    print("Авторизация выполнена успешно.")

# --- ФУНКЦИЯ ДЛЯ ВВОДА И ОТПРАВКИ ОТВЕТА ---
def submit_answer(browser):
    """Вводит и отправляет правильный ответ, при необходимости сбрасывая предыдущий"""

    # Ждем появления поля для ответа
    answer_input = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )

    # Проверяем, не заполнено ли поле (имеет ли оно значение)
    current_value = answer_input.get_attribute("value")

    # Если поле не пустое, ищем и нажимаем кнопку .again-btn
    if current_value and current_value.strip():
        print("Поле не пустое, ищем кнопку .again-btn...")
        try:
            # Ищем кнопку "Решить снова"
            again_button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn"))
            )
            again_button.click()
            print("Кнопка .again-btn нажата")

            # Ждем, пока поле очистится
            time.sleep(1)

            # Обновляем ссылку на поле (после сброса DOM может обновиться)
            answer_input = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
            )
        except:
            print("Кнопка .again-btn не найдена или не кликабельна")
            # Если кнопки нет, пробуем очистить поле программно
            try:
                answer_input.clear()
            except:
                browser.execute_script("arguments[0].value = '';", answer_input)
    else:
        # Поле пустое, просто очищаем для надежности
        try:
            answer_input.clear()
        except:
            browser.execute_script("arguments[0].value = '';", answer_input)

    # Ждем, когда поле станет интерактивным
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )

    # Вычисляем и вводим ответ
    answer = str(math.log(int(time.time())))

    try:
        answer_input.send_keys(answer)
    except:
        browser.execute_script(f"arguments[0].value = '{answer}';", answer_input)

    # Нажимаем кнопку отправки
    submit_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    submit_btn.click()
    print("Ответ отправлен")

# --- ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ФИДБЕКА ---
def get_feedback_text(browser):
    """Ожидает появления фидбека и возвращает его текст."""
    # Ждем, пока появится поле с результатом (после отправки)
    feedback_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    return feedback_element.text

#ОСНОВНОЙ ТЕСТ
@pytest.mark.parametrize("url", lessons)
def test_stepik_lessons(browser, url):
    # Данные для авторизации
    login = "davydovaksenia529@yandex.com"
    password = "1595qtot"

    browser.get(url)

    # 2. Выполняем авторизацию (если она требуется)
    # Простая проверка: если есть кнопка "Войти", то логинимся.
    login_to_stepik(browser, login, password)

    time.sleep(3)

    # 3. Отправляем правильный ответ
    submit_answer(browser)
    time.sleep(3)

    # 4. Получаем текст фидбека
    feedback_text = get_feedback_text(browser)

    # 5. Проверяем, что фидбек равен "Correct!"
    #    Если нет — тест упадет и мы соберем текст ошибки.
    assert feedback_text == "Correct!", f"Ожидался 'Correct!', но получен: '{feedback_text}'"


