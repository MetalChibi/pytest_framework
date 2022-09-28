from pytest import fixture

from selenium import webdriver


@fixture(scope='function')  # session, function, class etc
# session: all tests in one browser
# function: one browser per function/test
def browser():
    # setup
    browser = webdriver.Chrome()
    # instead of `return browser`:
    yield browser
    # teardown
    print("I am tearing down this browser")
