from os import getenv

from brownie.network.account import Accounts

class Account(object):

    MNEMONIC = 'MNEMONIC'

    def __init__(self, mnemonic:str=None):
        if not mnemonic:
            mnemonic = self._getMnemonic()
        
        self._account = Accounts().from_mnemonic(
            mnemonic, count=1, offset=0)

    @property
    def address(self):
        return self._account.address

    @property
    def brownieAccount(self):
        return self._account
    
    def _getMnemonic(self) -> str:
        mnemonic = getenv(Account.MNEMONIC, None)

        if not mnemonic:
            raise ValueError('undefined env variable {}'.format(Account.MNEMONIC))

        return mnemonic        