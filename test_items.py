from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    # собираем массив элементов кнопок на странице
    buttons = browser.find_elements(By.CSS_SELECTOR,
                                    "button.btn.btn-lg.btn-primary.btn-add-to-basket")

    # если есть хотя бы одна кнопка - тест пройден
    assert len(buttons) > 0, "No such button found on the page"

    # таймаут для визуальной проверки локализации кнопки для удобства рецензии
    # time.sleep(30)


if __name__ == "__main__":
    pytest.main()

# pytest --language=es test_items.py
