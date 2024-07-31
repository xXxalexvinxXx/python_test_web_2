import yaml
import pytest
from module import Site

# Загружаем тестовые данные из файла testdata.yaml
with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

def test_step1(site, x_selector1, x_selector2, x_selector3, btn_selector, err1):
    """
    Тест для проверки обработки ошибки при неверной авторизации.

    :param site: Экземпляр класса Site.
    :param x_selector1: XPath селектор для первого поля ввода.
    :param x_selector2: XPath селектор для второго поля ввода.
    :param x_selector3: XPath селектор для элемента с текстом ошибки.
    :param btn_selector: CSS селектор для кнопки.
    :param err1: Ожидаемый текст ошибки.
    """
    site.reset_site()
    input1 = site.find_element('xpath', x_selector1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    err_label = site.find_element('xpath', x_selector3)
    text = err_label.text
    assert text == err1

def test_step2(site, x_selector1, x_selector2, x_selector4, btn_selector, er2):
    """
    Тест для проверки успешной авторизации и получения имени пользователя.

    :param site: Экземпляр класса Site.
    :param x_selector1: XPath селектор для первого поля ввода.
    :param x_selector2: XPath селектор для второго поля ввода.
    :param x_selector4: XPath селектор для элемента с именем пользователя.
    :param btn_selector: CSS селектор для кнопки.
    :param er2: Ожидаемый текст приветствия.
    """
    site.reset_site()
    input1 = site.find_element('xpath', x_selector1)
    input1.clear()
    input1.send_keys(testdata['user'])
    input2 = site.find_element('xpath', x_selector2)
    input2.clear()
    input2.send_keys(testdata['pass'])
    btn = site.find_element('css', btn_selector)
    btn.click()
    user_label = site.find_element('xpath', x_selector4)
    text = user_label.text
    assert text == er2
