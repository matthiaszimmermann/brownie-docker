VALUE_INITIALIZED = 0

def test_owner_address(box, accounts):
    # verify that accounts[0] is contract owner
    assert accounts[0].address == box.owner()


def test_value_after_contract_creation(box, accounts):
    # verify initialized value of box
    assert VALUE_INITIALIZED == box.retrieve()

