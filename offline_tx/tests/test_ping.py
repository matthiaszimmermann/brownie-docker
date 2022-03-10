def test_state_after_deploy(pingContract, accounts):
    assert pingContract is not None
    assert pingContract.pings({'from': accounts[0]}) == 0
    assert pingContract.pingSum({'from': accounts[0]}) == 0

def test_single_ping(pingContract, accounts):
    pingContract.ping(42, {'from': accounts[0]})
    assert pingContract.pings({'from': accounts[0]}) == 1
    assert pingContract.pingSum({'from': accounts[0]}) == 42

def test_multiple_pings(pingContract, accounts):
    assert pingContract.pings({'from': accounts[0]}) == 0
    assert pingContract.pingSum({'from': accounts[0]}) == 0

    pingContract.ping(10, {'from': accounts[1]})
    pingContract.ping(20, {'from': accounts[2]})
    pingContract.ping(30, {'from': accounts[3]})

    assert pingContract.pings({'from': accounts[0]}) == 3
    assert pingContract.pingSum({'from': accounts[0]}) == 60
