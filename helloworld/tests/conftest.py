import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def box(Box, accounts):
    """
    returns box contract object deployed on ganache.
    contract owner is accounts[0]
    """
    return Box.deploy({'from': accounts[0]})
