
from brownie import (
    CounterControllerV1,
    CounterProxy,
    Contract,
)

from tests.const import (
    OWNER_ACCOUNT_NO,
    ADDER_ACCOUNT_NO,
    VALUE_INITIALIZED,
)

from tests.util import encode_function_data

def test_deploy_with_initializer(counterControllerV1, accounts):
    # deploy proxy with initializer call to ensure that controller is 
    # properly initialized (contract state hold in proxy, not controller)
    encoded_initializer = encode_function_data(initializer=counterControllerV1.initialize)
    proxy_ok = CounterProxy.deploy(counterControllerV1, encoded_initializer, {'from': accounts[OWNER_ACCOUNT_NO]})

    # cast proxy to counter
    counter = Contract.from_abi("CounterControllerV1", proxy_ok.address, CounterControllerV1.abi)
    assert counterControllerV1.value() == counter.value({'from': accounts[ADDER_ACCOUNT_NO]})


def test_deploy_without_initializer(counterControllerV1, accounts):
    # deploy counter w/o a call to initializer
    # as proxy has the whole state of the contract (and not the controller)
    # the proxy will then be in an uninitialized state
    empty_initializer = encode_function_data()
    proxy_error = CounterProxy.deploy(counterControllerV1, empty_initializer, {'from': accounts[OWNER_ACCOUNT_NO]})

    # cast proxy to counter
    counter = Contract.from_abi("CounterControllerV1", proxy_error.address, CounterControllerV1.abi)
    assert counterControllerV1.value() != counter.value({'from': accounts[ADDER_ACCOUNT_NO]})
    assert 0 == counter.value({'from': accounts[ADDER_ACCOUNT_NO]})
