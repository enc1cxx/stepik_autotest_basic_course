import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку: pytest -s
# -v -m smoke test_fixture5(mark tests).py Если всё сделано правильно, то должен запуститься только тест с маркировкой
# smoke. При этом вы увидите warning Это предупреждение появилось потому, что в последних версиях PyTest настоятельно
# рекомендуется регистрировать метки явно перед использованием. Как же регистрировать метки? Создайте файл pytest.ini
# в корневой директории вашего тестового проекта и добавьте в файл следующие строки:
# [pytest] markers =
#   smoke: marker for smoke tests
#   regression: marker for regression tests
#
# Текст после знака ":" является поясняющим — его можно не писать.
# Так же можно маркировать целый тестовый класс. В этом случае маркировка будет применена ко всем тестовым методам,
# входящим в класс.

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")