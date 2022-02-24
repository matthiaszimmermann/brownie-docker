import brownie
from hexbytes import HexBytes

from tests.const import DEFAULT_ADMIN_ROLE
from tests.const import ADDER_ROLE

from tests.const import OWNER_ACCOUNT_NO
from tests.const import ADDER1_ACCOUNT_NO
from tests.const import ADDER2_ACCOUNT_NO


def test_adder_transitive_granting(protectedCounter, accounts):

    # verify that role admin of adder_role is set to adder_role
    assert DEFAULT_ADMIN_ROLE != HexBytes(ADDER_ROLE)
    assert ADDER_ROLE == HexBytes(protectedCounter.getRoleAdmin(ADDER_ROLE))

    owner = accounts[OWNER_ACCOUNT_NO]
    adder_user_1 = accounts[ADDER1_ACCOUNT_NO]
    adder_user_2 = accounts[ADDER2_ACCOUNT_NO]

    # verify that adder_user_1 and user_1 cannot initially inc
    with brownie.reverts():
        protectedCounter.inc({'from': adder_user_1})

    with brownie.reverts():
        protectedCounter.inc({'from': adder_user_2})

    # verify that adder_user_1 cannot initially grant adder role to adder_user_2
    with brownie.reverts():
        protectedCounter.grantRole(ADDER_ROLE, adder_user_2, {'from': adder_user_1})

    # grant adder role to adder_user_1
    protectedCounter.grantRole(ADDER_ROLE, adder_user_1, {'from': owner})
    assert protectedCounter.hasRole(ADDER_ROLE, adder_user_1.address);

    # verify that adder_user_1 can and adder_user_2 cannot inc
    protectedCounter.inc({'from': adder_user_1})

    with brownie.reverts():
        protectedCounter.inc({'from': adder_user_2})

    # verify that adder_user_1 can now grant adder role to adder_user_2
    protectedCounter.grantRole(ADDER_ROLE, adder_user_2, {'from': adder_user_1})

    # verify that adder_user_1 and adder_user_1 can both inc
    protectedCounter.inc({'from': adder_user_1})
    protectedCounter.inc({'from': adder_user_2})
