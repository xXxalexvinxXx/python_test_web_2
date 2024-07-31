import pytest
import yaml
from module import Site

# Загрузка данных из файла testdata.yaml
with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

# Имя пользователя для использования в тестах
name = testdata['user']

@pytest.fixture(scope='module')
def site():
    """
    Фикстура для создания и закрытия экземпляра сайта.

    Создаёт экземпляр класса Site перед выполнением всех тестов в модуле.
    Закрывает браузер после выполнения всех тестов.
    """
    site = Site(testdata['address'])
    yield site
    site.close()

# Фикстуры для селекторов элементов на странице

@pytest.fixture()
def x_selector1():
    """
    Фикстура для получения селектора элемента ввода имени пользователя на странице входа.

    :return: XPath селектор элемента ввода имени пользователя.
    """
    return '//*[@id="login"]/div[1]/label/input'

@pytest.fixture()
def x_selector2():
    """
    Фикстура для получения селектора элемента ввода пароля на странице входа.

    :return: XPath селектор элемента ввода пароля.
    """
    return '//*[@id="login"]/div[2]/label/input'

@pytest.fixture()
def x_selector3():
    """
    Фикстура для получения селектора элемента для отображения сообщения об ошибке после неудачной авторизации.

    :return: XPath селектор элемента сообщения об ошибке.
    """
    return '//*[@id="app"]/main/div/div/div[2]/h2'

@pytest.fixture()
def x_selector4():
    """
    Фикстура для получения селектора элемента для отображения имени пользователя после успешной авторизации.

    :return: XPath селектор элемента имени пользователя.
    """
    return '//*[@id="app"]/main/nav/ul/li[3]/a'

@pytest.fixture()
def btn_selector():
    """
    Фикстура для получения CSS селектора кнопки на странице.

    :return: CSS селектор кнопки.
    """
    return 'button'

@pytest.fixture()
def err1():
    """
    Фикстура для получения ожидаемого текста сообщения об ошибке после неудачной авторизации.

    :return: Ожидаемый текст ошибки.
    """
    return '401'

@pytest.fixture()
def er2():
    """
    Фикстура для получения ожидаемого текста приветствия после успешной авторизации.

    :return: Ожидаемый текст приветствия.
    """
    return 'Hello, {}'.format(name)

# Фикстуры для элементов поста

@pytest.fixture()
def post_title_selector():
    """
    Фикстура для получения селектора поля ввода заголовка поста.

    :return: XPath селектор поля ввода заголовка поста.
    """
    return '//*[@id="post_title"]'

@pytest.fixture()
def post_description_selector():
    """
    Фикстура для получения селектора поля ввода описания поста.

    :return: XPath селектор поля ввода описания поста.
    """
    return '//*[@id="post_description"]'

@pytest.fixture()
def post_content_selector():
    """
    Фикстура для получения селектора поля ввода содержания поста.

    :return: XPath селектор поля ввода содержания поста.
    """
    return '//*[@id="post_content"]'

@pytest.fixture()
def create_post_button_selector():
    """
    Фикстура для получения селектора кнопки создания нового поста.

    :return: CSS селектор кнопки создания поста.
    """
    return 'button#create-post'

@pytest.fixture()
def save_post_button_selector():
    """
    Фикстура для получения селектора кнопки сохранения поста.

    :return: CSS селектор кнопки сохранения поста.
    """
    return 'button#save-post'

@pytest.fixture()
def new_post_title_selector():
    """
    Фикстура для получения селектора элемента для проверки заголовка нового поста.

    :return: XPath селектор элемента заголовка нового поста.
    """
    return '//*[@id="app"]/main/div[1]/h1'

# Фикстуры для данных поста

@pytest.fixture()
def post_title():
    """
    Фикстура для получения заголовка нового поста из файла конфигурации.

    :return: Заголовок нового поста.
    """
    return testdata['title']

@pytest.fixture()
def post_description():
    """
    Фикстура для получения описания нового поста из файла конфигурации.

    :return: Описание нового поста.
    """
    return testdata['descript']

@pytest.fixture()
def post_content():
    """
    Фикстура для получения содержания нового поста из файла конфигурации.

    :return: Содержание нового поста.
    """
    return testdata['cont']
