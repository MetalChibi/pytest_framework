from pytest import fixture

from selenium import webdriver


@fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    return browser
