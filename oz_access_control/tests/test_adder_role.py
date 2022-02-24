import brownie

from tests.const import DEFAULT_ADMIN_ROLE
from tests.const import ADDER_ROLE

from tests.const import OWNER_ACCOUNT_NO
from tests.const import ADDER1_ACCOUNT_NO
from tests.const import ADDER2_ACCOUNT_NO

def test_add_revoke_adder_role(protectedCounter, accounts):
    assert 1 == protectedCounter.getRoleMemberCount(ADDER_ROLE);

    owner = accounts[OWNER_ACCOUNT_NO]
    adder_user_1 = accounts[ADDER1_ACCOUNT_NO]
    adder_user_2 = accounts[ADDER2_ACCOUNT_NO]

    # check that role is not initially granted
    assert not protectedCounter.hasRole(ADDER_ROLE, adder_user_1.address);
    assert not protectedCounter.hasRole(ADDER_ROLE, adder_user_2.address);

    # grant role to two accounts
    protectedCounter.grantRole(ADDER_ROLE, adder_user_1, {'from': owner})
    protectedCounter.grantRole(ADDER_ROLE, adder_user_2, {'from': owner})

    # check role member enumeration
    assert 3 == protectedCounter.getRoleMemberCount(ADDER_ROLE);
    assert owner.address == protectedCounter.getRoleMember(ADDER_ROLE, 0);
    assert adder_user_1.address == protectedCounter.getRoleMember(ADDER_ROLE, 1);
    assert adder_user_2.address == protectedCounter.getRoleMember(ADDER_ROLE, 2);
    assert protectedCounter.hasRole(ADDER_ROLE, owner.address);
    assert protectedCounter.hasRole(ADDER_ROLE, adder_user_1.address);
    assert protectedCounter.hasRole(ADDER_ROLE, adder_user_2.address);

    # remove role from 1 account
    protectedCounter.revokeRole(ADDER_ROLE, adder_user_2, {'from': owner})

    # check updated role member enumeration
    assert 2 == protectedCounter.getRoleMemberCount(ADDER_ROLE);
    assert owner.address == protectedCounter.getRoleMember(ADDER_ROLE, 0);
    assert adder_user_1.address == protectedCounter.getRoleMember(ADDER_ROLE, 1);
    assert protectedCounter.hasRole(ADDER_ROLE, adder_user_1.address);
    assert not protectedCounter.hasRole(ADDER_ROLE, adder_user_2.address);


def test_adder_role_for_inc(protectedCounter, accounts):
    assert 1 == protectedCounter.getRoleMemberCount(ADDER_ROLE);

    owner = accounts[OWNER_ACCOUNT_NO]
    adder_user = accounts[ADDER1_ACCOUNT_NO]
    value_before = protectedCounter.value()

    protectedCounter.grantRole(ADDER_ROLE, adder_user, {'from': owner})

    # check if inc works
    protectedCounter.inc({'from': adder_user})

    # verify effect of inc on value
    assert value_before + 1 == protectedCounter.value()

    # check if dec fails
    with brownie.reverts():
        protectedCounter.dec({'from': adder_user})


def test_adding_fails_without_adder_role(protectedCounter, accounts):
    # verify that accounts[0] initially not allowed to inc()   with brownie.reverts():
    with brownie.reverts():
        protectedCounter.inc({'from': accounts[ADDER1_ACCOUNT_NO]})

