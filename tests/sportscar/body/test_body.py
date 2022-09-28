from pytest import mark


@mark.body
class BodyTests:
    @mark.smoke
    def test_body_functions_as_expected(self):
        assert True

    @mark.ui
    def test_can_navigate_to_body_page(self, browser):
        browser.get('http://motortrend.com/')
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
