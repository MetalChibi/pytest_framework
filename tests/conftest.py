from pytest import fixture
from selenium import webdriver
from config import Config
import json


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


# customize stuff

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against."
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

# pytest ... --env qa|dev|staging

@fixture(scope='session')
def app_config(env):
    return Config(env)


@fixture(params=[
    webdriver.Chrome,
    webdriver.Firefox
])
def many_browsers(request):
    driver = request.param
    yield driver()
    driver().quit()


# def load_test_data(path):
#     # with open(path) as data_file:
#     #     data = json.load(data_file)
#     #     return data
#     return json.load(open(path))
# @fixture(params=load_test_data("test_data.json"))


@fixture(params=json.load(open("./tests/test_data.json")))
def tv_brand(request):
    return request.param
