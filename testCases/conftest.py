import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):  # This will get ṭhe value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # This will return the browser value to setup method

"""
#######   Pytest HTML Report ######
# This hook will add env info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'TCW'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Mohit'


# This hook will delete/modify env info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
"""