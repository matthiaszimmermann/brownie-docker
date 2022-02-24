from tests.const import DEFAULT_ADMIN_ROLE
from tests.const import ADDER_ROLE

from tests.const import OWNER_ACCOUNT_NO
from tests.const import ADDER1_ACCOUNT_NO

from tests.const import VALUE_INITIALIZED

def test_value_after_contract_creation(protectedCounter, accounts):
    # verify initialized value of box
    assert VALUE_INITIALIZED == protectedCounter.value()

def test_admin_address(protectedCounter, accounts):
    owner = accounts[OWNER_ACCOUNT_NO]
    adder_user_1 = accounts[ADDER1_ACCOUNT_NO]

    # verify that accounts[OWNER_ACCOUNT_NO] is contract admin
    assert protectedCounter.hasRole(DEFAULT_ADMIN_ROLE, owner.address)
    assert protectedCounter.hasRole(ADDER_ROLE, owner.address)

    # verify that some other account (eg accounts[ADDER1_ACCOUNT_NO]) is not contract admin and does not have adder role
    assert not protectedCounter.hasRole(DEFAULT_ADMIN_ROLE, adder_user_1.address)
    assert not protectedCounter.hasRole(ADDER_ROLE, adder_user_1.address)

