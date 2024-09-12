import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser

    # Пост-условие: закрываем браузер после выполнения теста
    chrome_browser.quit()
