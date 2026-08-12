"""
Fixtures para los tests de Selenium
"""

import os
from typing import Generator
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(name="driver")
def fixture_driver() -> Generator:
    """Creamos el webdriver que vamos a usar en nuestros tests!"""
    posible_options = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions()
    }

    browser = os.getenv("TEST_BROWSER", "chrome").lower()
    # Si no existe la variable, dejamos None para saber que es local
    command_executor = os.getenv("TEST_COMMAND_EXECUTOR")
    options = posible_options[browser]

    # 🚀 Si hay una URL configurada, usamos Remote. Si no, abrimos navegador local.
    if command_executor:
        # Nota: Si usas Selenium 4, quita el '/wd/hub' de tu .env si te da error
        driver = webdriver.Remote(command_executor=command_executor, options=options)
    else:
        if browser == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Navegador no soportado localmente: {browser}")

    yield driver
