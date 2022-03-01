
from brownie import (
    CounterControllerV1,
    Contract,
)

from tests.const import (
    OWNER_ACCOUNT_NO,
    ADDER_ACCOUNT_NO,
    VALUE_INITIALIZED,
)

from tests.util import encode_function_data

def test_value_after_controller_v1_creation(counterControllerV1, accounts):
    # verify initialized value of box
    assert VALUE_INITIALIZED == counterControllerV1.value()

def test_value_after_proxy_creation(counterProxy, accounts):

    # cast proxy to counter v1
    counter_v1 = Contract.from_abi("CounterControllerV1", counterProxy.address, CounterControllerV1.abi)
    assert VALUE_INITIALIZED == counter_v1.value({'from': accounts[ADDER_ACCOUNT_NO]})
