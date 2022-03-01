import pytest

from tests.const import (
    OWNER_ACCOUNT_NO,
    VALUE_INITIALIZED_V2,
)

from tests.util import encode_function_data

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def counterControllerV1(CounterControllerV1, accounts):
    controller = CounterControllerV1.deploy({'from': accounts[OWNER_ACCOUNT_NO]})
    controller.initialize()
    return controller

@pytest.fixture(scope="module")
def counterControllerV2(CounterControllerV2, accounts):
    controller = CounterControllerV2.deploy({'from': accounts[OWNER_ACCOUNT_NO]})
    controller.initialize()
    return controller

@pytest.fixture(scope="module")
def counterProxy(CounterProxy, counterControllerV1, accounts):
    encoded_initializer = encode_function_data(initializer=counterControllerV1.initialize)
    return CounterProxy.deploy(counterControllerV1, encoded_initializer, {'from': accounts[OWNER_ACCOUNT_NO]})

@pytest.fixture(scope="module")
def counterProxyV2(counterProxy, counterControllerV2, accounts):
    encoded_upgrade = encode_function_data(
        VALUE_INITIALIZED_V2, 
        initializer=counterControllerV2.upgradeToV2
    )

    counterProxy.upgradeToAndCall(
        counterControllerV2.address, 
        encoded_upgrade, 
        {"from": accounts[OWNER_ACCOUNT_NO]}
    )

    return counterProxy

@pytest.fixture(scope="module")
def counterV2(Contract, CounterControllerV2, counterProxyV2):
    return Contract.from_abi("CounterControllerV2", counterProxyV2.address, CounterControllerV2.abi)
