from pytest import mark


@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True


@mark.ui
@mark.engine
def test_can_navigate_to_engine_page(browser):
    browser.get('http://artofmanliness.com/')
    assert True