from brownie import config

# map constants to brownie config
NETWORKS_DEV = ['development']
MNEMONIC_DEV = config['wallets']['owner_mnemonic_dev']

NETWORKS = config['networks']
MNEMONIC = config['wallets']['owner_mnemonic']

