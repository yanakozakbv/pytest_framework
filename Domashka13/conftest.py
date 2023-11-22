import pytest
from pytest_framework.Domashka13.car import Car


@pytest.fixture(scope='session')
def get_new_car():
    new_car = Car('Tesla', 'Model S')
    return new_car


@pytest.fixture(scope='session')
def get_new_limit_car():
    new_limit_car = Car('Tesla', 'Model S', 333)
    return new_limit_car
