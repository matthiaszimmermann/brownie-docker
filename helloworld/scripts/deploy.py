from brownie import Box, accounts, network

def main():
    account = accounts.load('deploy_account')
    contract = Box.deploy({'from': account})

    print('contract successfully deployed on network {}'.format(network.show_active()))
    print('initial box value {}'.format(contract.retrieve()))
    print('contract address {}'.format(contract.address))
    print('owner address {}'.format(account.address))
