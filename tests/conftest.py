from pytest import fixture
from selenium import webdriver
from config import Config

@fixture(scope='session')  # session, function, class etc
# session: all tests in one browser
# function: one browser per function/test
def browser():
    # setup
    browser = webdriver.Chrome()
    # instead of `return browser`:
    yield browser
    # teardown
    print("I am tearing down this browser")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against."
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
