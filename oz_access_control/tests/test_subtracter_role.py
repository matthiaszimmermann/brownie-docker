import brownie

from tests.const import DEFAULT_ADMIN_ROLE
from tests.const import SUBTRACTOR_ROLE

from tests.const import OWNER_ACCOUNT_NO
from tests.const import SUBTRACTOR_ACCOUNT_NO

def test_add_revoke_subtractor_role(protectedCounter, accounts):
    assert 0 == protectedCounter.getRoleMemberCount(SUBTRACTOR_ROLE);

    subtractor_user = accounts[SUBTRACTOR_ACCOUNT_NO]

    # check that role is not initially granted
    assert not protectedCounter.hasRole(SUBTRACTOR_ROLE, subtractor_user.address);

    # grant role
    protectedCounter.grantRole(SUBTRACTOR_ROLE, subtractor_user, {'from': accounts[OWNER_ACCOUNT_NO]})

    # check role member enumeration
    assert 1 == protectedCounter.getRoleMemberCount(SUBTRACTOR_ROLE);
    assert subtractor_user.address == protectedCounter.getRoleMember(SUBTRACTOR_ROLE, 0);
    assert protectedCounter.hasRole(SUBTRACTOR_ROLE, subtractor_user.address);

    # remove role
    protectedCounter.revokeRole(SUBTRACTOR_ROLE, subtractor_user, {'from': accounts[OWNER_ACCOUNT_NO]})

    # check updated role member enumeration
    assert 0 == protectedCounter.getRoleMemberCount(SUBTRACTOR_ROLE);
    assert not protectedCounter.hasRole(SUBTRACTOR_ROLE, subtractor_user.address);


def test_subtractor_role_for_dec(protectedCounter, accounts):
    assert 0 == protectedCounter.getRoleMemberCount(SUBTRACTOR_ROLE);

    subtractor_user = accounts[SUBTRACTOR_ACCOUNT_NO]
    value_before = protectedCounter.value()

    protectedCounter.grantRole(SUBTRACTOR_ROLE, subtractor_user, {'from': accounts[OWNER_ACCOUNT_NO]})

    # check if dec works
    protectedCounter.dec({'from': subtractor_user})

    # verify effect of inc on value
    assert value_before -1 == protectedCounter.value()

    # check if inc fails
    with brownie.reverts():
        protectedCounter.inc({'from': subtractor_user})


def test_dec_fails_without_subtractor_role(protectedCounter, accounts):
    # verify that accounts[0] initially not allowed to inc()   with brownie.reverts():
    with brownie.reverts():
        protectedCounter.dec({'from': accounts[OWNER_ACCOUNT_NO]})

