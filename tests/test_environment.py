import pytest
from pytest import mark
import unittest


def test_env_is_qa(app_config):
    assert app_config.base_url == "https://myqaenv.com"
    assert app_config.app_port == 80


@mark.xfail(reason="Env is not QA")
def test_env_is_dev(app_config):
    assert app_config.base_url == "https://mydevenv.com"
    assert app_config.app_port == 8080


@mark.skip("--env isn't staging")
def test_env_is_staging(app_config):
    assert app_config.base_url == "https://mystagingenv.com"
    assert app_config.app_port == 666


@mark.skip(reason="Just skipping this")
def test_skipped():
    pass


@mark.wip(reason="This test is WIP, not for production")
def test_wip():
    pass

