import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def answer():
    value = math.log(int(time.time()))
    return value


# @pytest.fixture(scope='function')
def reset(browser):
    time.sleep(5)
    x = browser.find_element(By.TAG_NAME, "textarea").get_attribute('disabled')
    if x:
        print(x, 'Сброс')
        browser.find_element(By.CLASS_NAME, 'again-btn').click()
    time.sleep(5)


@pytest.fixture(scope='session')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    link = "https://stepik.org"
    browser.get(link)
    browser.find_element(By.ID, "ember27").click()
    browser.find_element(By.NAME, "login").send_keys("") #add login
    browser.find_element(By.NAME, "password").send_keys("") #add password
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    time.sleep(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson',
                         ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                          'https://stepik.org/lesson/236897/step/1',
                          'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1',
                          'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1',
                          'https://stepik.org/lesson/236905/step/1'])
def test_login(browser, lesson):
    browser.get(lesson)

    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))

    reset(browser)

    browser.find_element(By.TAG_NAME, "textarea").send_keys(answer())
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert text == "Correct!", "Text != Correct!"

