import pytest
from pytest import mark
import unittest


#@mark.skip
def test_env_is_qa(app_config):
    if app_config == "qa":
        assert app_config.base_url == "https://myqaenv.com"
        assert app_config.app_port == 80
    elif app_config == "dev":
        assert app_config.base_url == "https://mydevenv.com"
        assert app_config.app_port == 8080
    elif app_config == "staging":
        assert app_config.base_url == "https://mystagingenv.com"
        assert app_config.app_port == 666
    else:
        # TODO: this shit doesn't work to check exceptions if I enter a wrong env, gonna need to figure that out
        try:
            app_config
        except Exception:
            pass


@mark.skip(reason="Just skipping this")
def test_skipped():
    pass

