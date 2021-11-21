
VALUE_99 = 99
VALUE_100 = 100

def test_inc_below_100(box):

    # change box value
    box.store(VALUE_99)

    # verify value has changed
    assert VALUE_99 == box.retrieve()

    # increment box value
    box.inc()

    # verify value has been incremented
    assert VALUE_99 + 1 == box.retrieve()

def test_inc_below_100_not_owner(box, accounts):

    not_owner = accounts[1]

    # change box value
    box.store(VALUE_99)

    # verify value has changed
    assert VALUE_99 == box.retrieve()

    # increment box value
    box.inc({'from': not_owner})

    # verify value has been incremented
    assert VALUE_99 + 1 == box.retrieve()


def test_inc_at_100(box):

    # change box value
    box.store(VALUE_100)

    # verify value has changed
    assert VALUE_100 == box.retrieve()

    # increment box value
    box.inc()

    # verify value has not been incremented
    assert VALUE_100 == box.retrieve()
