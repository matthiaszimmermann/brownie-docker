
from brownie import (
    CounterControllerV1,
    CounterControllerV2,
    CounterControllerV3,
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

def test_controller_v3(accounts):
    controller = CounterControllerV3.deploy({'from': accounts[OWNER_ACCOUNT_NO]})
    controller.initialize()
    controller.upgradeToV2(VALUE_INITIALIZED_V2)
    controller.upgradeToV3()
    assert 3 == controller.version()
    assert VALUE_INITIALIZED_V2 == controller.value()
    assert VALUE_INITIALIZED == controller.previousValue()

def test_upgrade_v3(counterProxyV2, accounts):
    # cast proxy to counter controller v2
    owner = accounts[OWNER_ACCOUNT_NO]
    adder = accounts[ADDER_ACCOUNT_NO]
    counter = Contract.from_abi("CounterControllerV2", counterProxyV2.address, CounterControllerV2.abi)

    # verify counter version before upgrade
    assert 2 == counter.version({'from': adder})

    # deploy upgraded controller
    counterControllerV3 = CounterControllerV3.deploy({'from': owner})

    # encode upgrade function
    encoded_upgrade = encode_function_data(
        # VALUE_INITIALIZED_V2, 
        initializer=counterControllerV3.upgradeToV3
    )

    # upgrade controller logic to v2, 
    # include call to upgrade proxy state
    counterProxyV2.upgradeToAndCall(
        counterControllerV3.address, 
        encoded_upgrade, 
        {"from": owner}
    )

    # cast proxy to counter controller v2
    counter = Contract.from_abi("CounterControllerV3", counterProxyV2.address, CounterControllerV3.abi)

    # verify counter version after upgrade
    assert 3 == counter.version({'from': adder})

    # verify functionality of inc() after upgrade
    counter.inc({'from': adder})
    counter.inc({'from': adder})
    assert VALUE_INITIALIZED_V2 + 2 == counter.value({'from': adder})
    assert VALUE_INITIALIZED_V2 + 1 == counter.previousValue({'from': adder})

    # verify functionality of dec() after upgrade
    counter.dec({'from': adder})
    assert VALUE_INITIALIZED_V2 + 1 == counter.value({'from': adder})
    assert VALUE_INITIALIZED_V2 + 2 == counter.previousValue({'from': adder})
