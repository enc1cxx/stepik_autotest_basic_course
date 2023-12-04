import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Параметризация тестов PyTest позволяет запустить один и тот же тест с разными входными параметрами. Для этого
# используется декоратор @pytest.mark.parametrize(). Наш сайт доступен для разных языков. Напишем тест,
# который проверит, что для сайта с русским и английским языком будет отображаться ссылка на форму логина. Передадим
# в наш тест ссылки на русскую и английскую версию главной страницы сайта.
# Дополнительно, полезный туториал из документации: Parametrizing fixtures and test functions
# https://docs.pytest.org/en/latest/how-to/parametrize.html?highlight=parametrize

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")