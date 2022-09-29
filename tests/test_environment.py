from pytest import mark


def test_env_is_qa(app_config):
    assert app_config.base_url == "https://myqaenv.com"
    assert app_config.app_port == 80

def test_env_is_dev(app_config):
    assert app_config.base_url == "https://mydevenv.com"
    assert app_config.app_port == 8080