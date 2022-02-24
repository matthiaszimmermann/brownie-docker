from brownie import Box, accounts, network


def pp_event(event, prefix='') -> str:
    lines = []
    for i, log in enumerate(event):
        lines.append('{}log[{}]'.format(prefix, i))
        for key, value in log.items():
            lines.append('{}  {}: {}'.format(prefix, key, value))
    
    return '\n'.join(lines)


def pp_events(events, prefix='') -> str:
    lines = []
    for key, event in events.items():
        lines.append('{}{}\n{}'.format(prefix, key, pp_event(event, '{}  '.format(prefix))))
    
    return '\n'.join(lines)


def main():
    account = accounts[0]
    contract = Box.deploy({'from': account})

    print('contract successfully deployed on network {}'.format(network.show_active()))
    print('initial box value {}'.format(contract.retrieve()))
    print('contract address {}'.format(contract.address))
    print('owner address {}'.format(account.address))

    tx = contract.inc()
    events = tx.events

    print('new box value {}'.format(contract.retrieve()))
    print('recored events\n{}'.format(events))
    print('events from tx.inc()\n{}'.format(pp_events(tx.events)))
