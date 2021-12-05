from brownie import CryptoStampPolygon, Contract, network

# address from pf (matches opensea contract address)
# https://crypto-stamp.post.ch/en/questions-and-answers
PROXY_CONTRACT_ADDRESS = '0x6ddcc90614d47acd7596447686c4fd6aee782742'
# address from log upgraded(newImpl)
STAMP_CONTRACT_ADDRESS = '0xbd481f5345f41aaeaac2a72f0ae22fab89f170d2'

EXAMPLE_STAMP_ACCOUNT_ADDRESS = '0xf3e3d5412aad4172e4d1fd39e7f912a11f2f0cbd'
EXAMPLE_STAMP_NFT_ID = 1

def main():
    proxy_contract = Contract.from_abi(CryptoStampPolygon._name, PROXY_CONTRACT_ADDRESS, CryptoStampPolygon.abi)
    stamp_contract = Contract.from_abi(CryptoStampPolygon._name, STAMP_CONTRACT_ADDRESS, CryptoStampPolygon.abi)
    
    print('current network: {}'.format(network.show_active()))
    print('proxy.totalSupply(1): {}'.format(proxy_contract.totalSupply(1)))
    print('proxy.totalSupply(2): {}'.format(proxy_contract.totalSupply(2)))
    print('proxy.totalSupply(3): {}'.format(proxy_contract.totalSupply(3)))
    print('proxy.totalSupply(4): {}'.format(proxy_contract.totalSupply(4)))
    print('proxy.totalSupply(5): {}'.format(proxy_contract.totalSupply(5)))
    print('proxy.totalSupply(6): {}'.format(proxy_contract.totalSupply(6)))
    print('proxy.totalSupply(7): {}'.format(proxy_contract.totalSupply(7)))
    print('proxy.totalSupply(8): {}'.format(proxy_contract.totalSupply(8)))
    print('proxy.totalSupply(9): {}'.format(proxy_contract.totalSupply(9)))
    print('proxy.totalSupply(10): {}'.format(proxy_contract.totalSupply(10)))
    print('proxy.totalSupply(11): {}'.format(proxy_contract.totalSupply(11)))
    print('proxy.totalSupply(12): {}'.format(proxy_contract.totalSupply(12)))
    print('proxy.totalSupply(13): {}'.format(proxy_contract.totalSupply(13)))
    
    print('sample stamp account: {}'.format(EXAMPLE_STAMP_ACCOUNT_ADDRESS))
    print('proxy.balanceOf({}, {}): {}'.format(
        EXAMPLE_STAMP_ACCOUNT_ADDRESS,
        EXAMPLE_STAMP_NFT_ID,
        proxy_contract.balanceOf(
            EXAMPLE_STAMP_ACCOUNT_ADDRESS, 
            EXAMPLE_STAMP_NFT_ID)))
    
    # why doesn't this work ???
    # print('???')
    # print('stamp.balanceOf(...): {}'.format(
    #     stamp_contract.balanceOf(
    #         EXAMPLE_STAMP_ACCOUNT_ADDRESS, 
    #         EXAMPLE_STAMP_NFT_ID)))