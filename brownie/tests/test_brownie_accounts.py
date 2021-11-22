import pytest

import eth_account # https://github.com/ethereum/eth-account

from brownie.network.account import Accounts # https://github.com/eth-brownie

ADDRESS_LENGTH = 42
ADDRESS_PREFIX = '0x'

DEFAULT_PATH = "m/44'/60'/0'/0/0"
MNEMONIC_NUM_WORDS = 12

ACCOUNT_MNEMONIC = 'candy maple cake sugar pudding cream honey rich smooth crumble sweet treat'
ACCOUNT_ADDRESS = '0x627306090abaB3A6e1400e9345bC60c78a8BEf57'
ACCOUNT_PRIVATE_KEY = '0xc87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3'

KEYSTORE_DIR = 'keystores'
KEYSTORE_FILE = 'keystore.json'
KEYSTORE_FILE2 = 'keystore2.json'
KEYSTORE_PASSWORD = 'keystore password'

@pytest.fixture
def enable_hd_wallet_features():
    eth_account.Account.enable_unaudited_hdwallet_features()

@pytest.fixture
def accounts():
    return Accounts()

@pytest.fixture
def candy_maple_account(accounts):
    return accounts.from_mnemonic(
        mnemonic=ACCOUNT_MNEMONIC, 
        count=1,
        offset=0,
        passphrase='')

@pytest.fixture(scope="session")
def keystore_file(tmpdir_factory):
    return tmpdir_factory.mktemp(KEYSTORE_DIR).join(KEYSTORE_FILE)

@pytest.fixture(scope="session")
def keystore_file2(tmpdir_factory):
    return tmpdir_factory.mktemp(KEYSTORE_DIR).join(KEYSTORE_FILE2)


def test_add(accounts: Accounts):
    print('add account [brownie] with new random mnemonic')

    account = accounts.add()

    assert account.address
    assert ADDRESS_LENGTH == len(account.address)
    assert '0x' == account.address[:2]

    print('account address: {}'.format(account.address))

    assert account.private_key
    print('account private key: {}'.format(account.private_key))


def test_from_mnemonic(candy_maple_account):
    print('create account [brownie] with provided mnemonic: {}'.format(ACCOUNT_MNEMONIC))
    
    assert candy_maple_account
    assert ACCOUNT_ADDRESS == candy_maple_account.address
    assert ACCOUNT_PRIVATE_KEY == candy_maple_account.private_key


def test_save_and_load(accounts, candy_maple_account, keystore_file):
    print('save account into keystore file {}'.format(str(keystore_file)))
    candy_maple_account.save(keystore_file, password=KEYSTORE_PASSWORD)

    print('load account from keystore')
    account = accounts.load(keystore_file, password=KEYSTORE_PASSWORD)
    
    assert account
    assert ACCOUNT_ADDRESS == account.address
    assert ACCOUNT_PRIVATE_KEY == account.private_key


def test_save_and_load_with_bad_password(accounts, candy_maple_account, keystore_file2):
    print('save account into keystore file {}'.format(str(keystore_file2)))
    candy_maple_account.save(keystore_file2, password=KEYSTORE_PASSWORD)

    bad_password = KEYSTORE_PASSWORD + ' :-('
    print('load account from keystore with bad password:"{}"'.format(bad_password))

    with pytest.raises(ValueError, match='MAC mismatch'):
        account = accounts.load(keystore_file2, password=bad_password)
