import pytest

from tests.const import OWNER_ACCOUNT_NO


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def protectedCounter(ProtectedCounter, accounts):
    """
    returns protectedCounter contract object deployed on ganache.
    """
    return ProtectedCounter.deploy({'from': accounts[OWNER_ACCOUNT_NO]})
