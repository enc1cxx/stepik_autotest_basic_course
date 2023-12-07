from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# Сначала установим плагин в нашем виртуальном окружении. После установки плагин будет автоматически найден PyTest,
# и можно будет пользоваться его функциональностью без дополнительных изменений кода:
#
# pip install pytest-rerunfailures

# Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:
# "--reruns n", где n — это количество перезапусков. Если при повторных запусках тесты пройдут успешно, то и прогон
# тестов будет считаться успешным. Количество перезапусков отображается в отчёте, благодаря чему можно позже
# анализировать проблемные тесты.

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")