
VALUE_99 = 99
VALUE_100 = 100

def test_inc(box):

    value_before = box.retrieve()

    # increment box value
    # should emit single LogValueChanged event
    tx = box.inc()
    events = tx.events.items()

    print('value before {}'.format(value_before))
    print('new value {}'.format(box.retrieve()))
    print('events\n{}'.format(events))

    assert 1 == len(events)


def test_store(box):

    # change box value
    tx = box.store(VALUE_99)
    events = tx.events.items()
    print('events\n{}'.format(events))
