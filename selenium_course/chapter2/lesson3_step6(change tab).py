import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element(By.ID, "input_value").text

    browser.find_element(By.ID, "answer").send_keys(calc(number))

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
