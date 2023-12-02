import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Name")

    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Lastname")

    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("Email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
