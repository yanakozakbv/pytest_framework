import pytest
from pytest_framework.constants import ROOT_PATH
from pytest_framework.db.sqlite_pack.cosmetics_repo import CosmeticsRepo


@pytest.fixture
def cosmetics_repo():
    return CosmeticsRepo(f"{ROOT_PATH}\\db\\test.db")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )
    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )
    config.addinivalue_line(
        "markers", "negative: mark test negative"
    )