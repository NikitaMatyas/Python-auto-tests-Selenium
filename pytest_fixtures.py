import pytest


@pytest.fixture()
def before():
    print('Once before every method')
    return 5


@pytest.fixture()
def after():
    yield
    print('After every method')


def testmethod1(before, after):
    print('This is testmethod1')
    assert before == 5
