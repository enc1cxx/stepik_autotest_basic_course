import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sum = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    print(sum)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum))

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
