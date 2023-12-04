from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class UnittestStyle(unittest.TestCase):
    def test_registration_1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Ivanov")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(
                "darkkillergandjubass@gmail.com")
            browser.find_element(By.CSS_SELECTOR, ".second_block  .form-control.first").send_keys("777777777")
            browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second").send_keys("Smol")
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            # находим элемент, содержащий текст
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be equal")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Ivanov")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(
                "darkkillergandjubass@gmail.com")
            browser.find_element(By.CSS_SELECTOR, ".second_block  .form-control.first").send_keys("777777777")
            browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second").send_keys("Smol")
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            # находим элемент, содержащий текст
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be equal")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
