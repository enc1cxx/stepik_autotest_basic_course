from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap").text

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
