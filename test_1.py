import yaml
import time

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
    time.sleep(testdata['sleep_time'])
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


def test_step3(site, x_selector1, x_selector2, x_selector4, create_post_button_selector,
               post_title_selector, post_description_selector, post_content_selector,
               save_post_button_selector, new_post_title_selector,
               post_title, post_description, post_content, btn_selector, er2):
    """
    Проверка создания и сохранения поста после авторизации.

    1. Выполняем шаг 2 для авторизации.
    2. Нажимаем кнопку для создания нового поста.
    3. Заполняем поля нового поста.
    4. Нажимаем кнопку для сохранения поста.
    5. Проверяем заголовок нового поста.

    :param site: Экземпляр класса Site.
    :param x_selector1: XPath для первого поля ввода (используется в шаге 2).
    :param x_selector2: XPath для второго поля ввода (используется в шаге 2).
    :param x_selector4: XPath для элемента после авторизации (используется в шаге 2).
    :param create_post_button_selector: CSS локатор кнопки создания поста.
    :param post_title_selector: XPath для поля заголовка поста.
    :param post_description_selector: XPath для поля описания поста.
    :param post_content_selector: XPath для поля содержания поста.
    :param save_post_button_selector: CSS локатор кнопки сохранения поста.
    :param new_post_title_selector: XPath для заголовка нового поста.
    :param post_title: Заголовок нового поста.
    :param post_description: Описание нового поста.
    :param post_content: Содержание нового поста.
    """
    # Выполнение шаг 1 (авторизация)
    # time.sleep(testdata['sleep_time'])
    # site.reset_site()
    # input1 = site.find_element('xpath', x_selector1)
    # input1.clear()
    # input1.send_keys(testdata['user'])
    # input2 = site.find_element('xpath', x_selector2)
    # input2.clear()
    # input2.send_keys(testdata['pass'])
    # btn = site.find_element('css', btn_selector)
    # btn.click()

    # Ожидание кнопки создания поста и её клик
    site.wait_for_element('css', create_post_button_selector)
    create_post_btn = site.find_element('css', create_post_button_selector)
    create_post_btn.click()

    # Ожидание появления полей для создания поста
    site.wait_for_element('xpath', post_title_selector)

    # Заполнение полей нового поста
    post_title_input = site.find_element('xpath', post_title_selector)
    post_title_input.clear()
    post_title_input.send_keys(post_title)

    post_description_input = site.find_element('xpath', post_description_selector)
    post_description_input.clear()
    post_description_input.send_keys(post_description)

    post_content_input = site.find_element('xpath', post_content_selector)
    post_content_input.clear()
    post_content_input.send_keys(post_content)

    # Ожидание кнопки сохранения поста и её клик
    site.wait_for_element('css', save_post_button_selector)
    save_post_btn = site.find_element('css', save_post_button_selector)
    save_post_btn.click()
    time.sleep(testdata['sleep_time'])
    site.refresh_site()

    # Ожидание заголовка нового поста и проверка его текста
    site.wait_for_element('xpath', new_post_title_selector)
    new_post_title = site.find_element('xpath', new_post_title_selector)
    response = new_post_title.text
    assert response == post_title
