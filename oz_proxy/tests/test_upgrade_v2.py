
from brownie import (
    CounterControllerV1,
    CounterControllerV2,
    CounterProxy,
    Contract,
    reverts,
)

from tests.const import (
    OWNER_ACCOUNT_NO,
    ADDER_ACCOUNT_NO,
    VALUE_INITIALIZED,
    VALUE_INITIALIZED_V2,
)

from tests.util import encode_function_data

def test_before_upgrade(counterProxy, accounts):
    counter = Contract.from_abi("CounterControllerV1", counterProxy.address, CounterControllerV1.abi)
    assert VALUE_INITIALIZED == counter.value({'from': accounts[ADDER_ACCOUNT_NO]})

def test_controller_v2(accounts):
    counter = CounterControllerV2.deploy({'from': accounts[OWNER_ACCOUNT_NO]})
    counter.initialize()
    counter.upgradeToV2(VALUE_INITIALIZED_V2)
    assert VALUE_INITIALIZED_V2 == counter.value()
    assert VALUE_INITIALIZED == counter.previousValue()

def test_upgrade_v2(counterProxy, accounts):
    # cast proxy to counter controller v2
    owner = accounts[OWNER_ACCOUNT_NO]
    adder = accounts[ADDER_ACCOUNT_NO]
    counter = Contract.from_abi("CounterControllerV1", counterProxy.address, CounterControllerV1.abi)

    # verify counter version before upgrade
    assert 1 == counter.version({'from': adder})

    # deploy upgraded controller
    counterControllerV2 = CounterControllerV2.deploy({'from': owner})

    # encode upgrade function
    encoded_upgrade = encode_function_data(
        VALUE_INITIALIZED_V2, 
        initializer=counterControllerV2.upgradeToV2
    )

    # upgrade controller logic to v2, 
    # include call to upgrade proxy state
    counterProxy.upgradeToAndCall(
        counterControllerV2.address, 
        encoded_upgrade, 
        {"from": owner}
    )

    # cast proxy to counter controller v2
    counter = Contract.from_abi("CounterControllerV2", counterProxy.address, CounterControllerV2.abi)

    # verify counter version after upgrade
    assert 2 == counter.version({'from': adder})

    # ensure calling upgrade a second time fails
    with reverts():
        counter.upgradeToV2(13, {"from": adder})

    # ensure it does not matter if owner or adder is calling upgrade
    with reverts():
        counter.upgradeToV2(13, {"from": owner})

    # check state and methods after upgrade to v2
    assert VALUE_INITIALIZED_V2 == counter.value({'from': adder})
    assert VALUE_INITIALIZED == counter.previousValue({'from': adder})

    # verify functionality of inc() after upgrade
    counter.inc({'from': adder})
    assert VALUE_INITIALIZED_V2 + 1 == counter.value({'from': adder})
    assert VALUE_INITIALIZED_V2 == counter.previousValue({'from': adder})
