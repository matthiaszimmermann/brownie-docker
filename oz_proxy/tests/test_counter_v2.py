
# from brownie import (
#     CounterControllerV1,
#     Contract,
# )

from tests.const import (
    # OWNER_ACCOUNT_NO,
    ADDER_ACCOUNT_NO,
    VALUE_INITIALIZED,
    VALUE_INITIALIZED_V2,
)

# from tests.util import encode_function_data

def test_intial_state(counterV2, accounts):
    adder = accounts[ADDER_ACCOUNT_NO]
    assert 2 == counterV2.version({'from': adder})
    assert VALUE_INITIALIZED == counterV2.previousValue({'from': adder})
    assert VALUE_INITIALIZED_V2 == counterV2.value({'from': adder})

def test_inc(counterV2, accounts):
    adder = accounts[ADDER_ACCOUNT_NO]

    counterV2.inc({'from': adder})
    assert VALUE_INITIALIZED_V2 + 1 == counterV2.value({'from': adder})
    assert VALUE_INITIALIZED_V2 == counterV2.previousValue({'from': adder})
