from pytest import mark


@mark.entertainment
def test_entertainment_functions_as_expected():
    assert True


@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(browser):
    browser.get('http://siriusxm.com/')
    assert True
