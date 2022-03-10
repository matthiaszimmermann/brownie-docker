import pytest

from brownie.network.account import Account

from scripts.util import (
    get_owner_account,
)

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def owner(accounts) -> Account:
    owner = get_owner_account()
    accounts[3].transfer(owner, "10 ether")
    return owner

@pytest.fixture(scope="module")
def pingContract(Ping, owner):
    return Ping.deploy({'from': owner})
