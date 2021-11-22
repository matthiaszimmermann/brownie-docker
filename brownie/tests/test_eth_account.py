import eth_account # https://github.com/ethereum/eth-account
import pytest

from eth_account.hdaccount import ETHEREUM_DEFAULT_PATH
from hexbytes import HexBytes

ADDRESS_LENGTH = 42
ADDRESS_PREFIX = '0x'

DEFAULT_PATH = "m/44'/60'/0'/0/0"
MNEMONIC_NUM_WORDS = 12

ACCOUNT_MNEMONIC = 'candy maple cake sugar pudding cream honey rich smooth crumble sweet treat'
ACCOUNT_ADDRESS = '0x627306090abaB3A6e1400e9345bC60c78a8BEf57'
ACCOUNT_PRIVATE_KEY = '0xc87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3'


@pytest.fixture
def enable_hd_wallet_features():
    eth_account.Account.enable_unaudited_hdwallet_features()


def test_hdwallet_path_default():
    print('check hd wallet default path for {}'.format(DEFAULT_PATH))
    assert DEFAULT_PATH == ETHEREUM_DEFAULT_PATH


def test_create():
    print('create account with new random mnemonic')

    account, mnemonic = eth_account.Account.create_with_mnemonic(
        passphrase = '',
        num_words = MNEMONIC_NUM_WORDS,
        language = 'english',
        account_path = ETHEREUM_DEFAULT_PATH
    )

    print('mnemonic: {}'.format(mnemonic))
    assert mnemonic
    assert MNEMONIC_NUM_WORDS == len(mnemonic.split(' '))

    print('account address: {}'.format(account.address))
    assert account
    assert account.address
    assert ADDRESS_LENGTH == len(account.address)
    assert '0x' == account.address[:2]

    assert account.key
    key = HexBytes(account.key).hex()
    print('account private key: {}'.format(key))


def test_from_mnemonic():
    print('create account with provided mnemonic: {}'.format(ACCOUNT_MNEMONIC))
    account = eth_account.Account.from_mnemonic(
        ACCOUNT_MNEMONIC, 
        passphrase='', 
        account_path=ETHEREUM_DEFAULT_PATH)
    
    assert account
    assert ACCOUNT_ADDRESS == account.address
    assert ACCOUNT_PRIVATE_KEY == HexBytes(account.key).hex()