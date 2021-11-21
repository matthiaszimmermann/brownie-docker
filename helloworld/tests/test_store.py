import brownie

from test_deploy import VALUE_INITIALIZED

# openzeppelin ownable revert string 
REVERT_NOT_OWNER = 'Ownable: caller is not the owner'

VALUE_CHANGED = 11

def test_change_value(box, accounts):

    # verify initialized value of box
    assert VALUE_INITIALIZED == box.retrieve()

    # change box value
    box.store(VALUE_CHANGED)

    # verify value has changed
    assert VALUE_CHANGED == box.retrieve()


def test_change_value_different_accounts(box, accounts):

    owner = accounts[0]
    not_owner = accounts[1]

    # verify that owner may change box value
    change_value(box, owner, 1)
    assert 1 == box.retrieve()

    # verify that non-owner account may not change box value
    with brownie.reverts(REVERT_NOT_OWNER):
        change_value(box, not_owner, VALUE_CHANGED)


def change_value(box, account, new_value):
    box.store(new_value, {'from': account})
