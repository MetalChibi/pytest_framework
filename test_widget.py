from pytest import mark


def test_widget_functions_as_expected():
    assert True

@mark.xfail
def test_widget_fails():
    assert False
