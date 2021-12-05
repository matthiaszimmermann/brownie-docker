import eth_account
import sys

from brownie.network.account import Accounts


ADDRESS_FILE = './keystore.address'
MNEMONIC_FILE = './keystore.mnemonic'
KEYSTORE_FILE = './keystore.json'


def main():
    if len(sys.argv) != 2:
        print('usage: {} keystore-password-file'.format(sys.argv[0]))
        sys.exit(1)

    # create mnemonic
    eth_account.Account.enable_unaudited_hdwallet_features()
    _, mnemonic = eth_account.Account.create_with_mnemonic()

    # retrieve command line args
    password_file = sys.argv[1]

    # create account
    accounts = Accounts()
    account = accounts.from_mnemonic(
        mnemonic=mnemonic, 
        count=1,
        offset=0,
        passphrase='')
    
    # write address file and mnemonic
    with open(ADDRESS_FILE, 'w') as fa:
        fa.write(account.address)
        
    # write address file and mnemonic
    with open(MNEMONIC_FILE, 'w') as fm:
        fm.write('{}\n'.format(mnemonic))

    # read keystore-password
    password = ''
    with open(password_file) as fp:
        lines = fp.readlines()
        password = lines[0].strip()
        
    # export to keystore
    account.save(KEYSTORE_FILE, password=password)


if __name__ == "__main__":
    main()
