import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Загрузка данных из конфигурационного файла
with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


class Site:
    def __init__(self, address):
        """
        Инициализация драйвера и открытие указанного адреса.

        :param address: URL адрес сайта для тестирования.
        """
        # Настройка драйвера в зависимости от выбранного браузера
        if browser == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        # Настройка ожидания и размера окна
        self.driver.implicitly_wait(testdata['wait'])
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata['sleep_time'])

    def find_element(self, mode, path):
        """
        Поиск элемента на странице.

        :param mode: Метод локализации элемента ('css' или 'xpath').
        :param path: Локатор элемента.
        :return: Найденный элемент.
        """
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def wait_for_element(self, mode, path, timeout=10):
        """
        Ожидание появления элемента на странице.

        :param mode: Метод локализации элемента ('css' или 'xpath').
        :param path: Локатор элемента.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Найденный элемент.
        """
        if mode == 'css':
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, path))
            )
        elif mode == 'xpath':
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
        else:
            raise ValueError(f"Unsupported mode: {mode}")
        return self.find_element(mode, path)

    def get_element_property(self, mode, path, property):
        """
        Получение значения CSS свойства элемента.

        :param mode: Метод локализации элемента ('css' или 'xpath').
        :param path: Локатор элемента.
        :param property: Имя CSS свойства.
        :return: Значение CSS свойства.
        """
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        """
        Закрытие браузера.
        """
        self.driver.close()

    def reset_site(self):
        """
        Перезагрузка сайта.
        """
        self.driver.get(testdata['address'])
        time.sleep(testdata['sleep_time'])

    def refresh_site(self):
        self.driver.refresh()

