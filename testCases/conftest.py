import pytest
from selenium import webdriver
from utilities import createlog


@pytest.fixture(autouse=True, scope='session')
def setlogs():
    createlog.LogGen2.loggen()


@pytest.fixture()
def setup(browser):
    global driver
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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True)
def tear_down(request):
    yield
    item = request.node
    if item.rep_call.failed:
        driver.save_screenshot(str(item.name)+'.png')
    driver.close()


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
