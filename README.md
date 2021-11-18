# brownie-docker
docker based brownie development

## links

* tutorial on [medium](https://iamdefinitelyahuman.medium.com/getting-started-with-brownie-part-1-9b2181f4cb99)
* working with [accounts](https://eth-brownie.readthedocs.io/en/stable/account-management.html)
* working with [networks](https://eth-brownie.readthedocs.io/en/stable/network-management.html)
* brownie [github](https://github.com/eth-brownie/brownie)

## build the docker image

docker file based on brownie's [Dockerfile](https://github.com/eth-brownie/brownie/blob/master/Dockerfile), and corresponding requirements.txt

build the docker image

```bash
docker build -t brownie .
```

## run docker container

run docker container in interactive mode

```bash
docker run -it --rm -v $PWD/accounts:/accounts brownie
```

inside the container you can now work with brownie.

## use brownie

### create and use local accounts

start brownie in console mode

```bash
brownie console
```

inside the brownie console create a new account and save it into a keystore file.

```bash
>>> test_account = accounts.add()
mnemonic: 'fold tobacco uncle egg view main merge focus clog roast ostrich unlock'
>>> test_account.address
'0xd05bF11e7764e59B4D5B3f1a7c25f2087D1b3931'
>>> test_account.save('/accounts/test_account.json', password='test')
```

the commands above lead to a keystore file `/accounts/test_account.json` for the account.
note that the command `accounts.add()` will create a new mnemonic phrase with every call.

this account can then be reused in a new brownie session as shown below.
as shown, the address of the account loaded from the keystore file matches
with the accoun address created above.

```bash
>>> test_account = accounts.load('/accounts/test_account.json', password='test')
>>> test_account.address
'0xd05bF11e7764e59B4D5B3f1a7c25f2087D1b3931'
```

an account may also be created by providing a mnemonic sentence.
when used as shown below, the mapping from mnemonic to account address matches with metamask.
accounts can also be saved using just an id ('candy' in the example below)

```bash
>>> candy_account = accounts.from_mnemonic('candy maple cake sugar pudding cream honey rich smooth crumble sweet treat', passphrase='')
>>> candy_account.address
'0x627306090abaB3A6e1400e9345bC60c78a8BEf57'
candy_account.save('candy', password='maple')
'/root/.brownie/accounts/candy.json'
```

local accounts that are saved in brownies' default location become visible to brownies account management (outside the console)

```bash
brownie accounts list
Brownie v1.17.1 - Python development framework for Ethereum

Found 1 account:
 └─candy: 0x627306090abaB3A6e1400e9345bC60c78a8BEf57
```

### connect to mainnet

example: check the balance of an mainnet address with a large amount of ethers.
check the balance on etherscan

https://etherscan.io/address/0x00000000219ab540356cbb839cbe05303d7705fa

now, compare the balance using brownie console as shown below.
to have brownie connect to mainnet use [infura](https://infura.io) and pass the infura project id via environment variable to brownie.

```bash
export WEB3_INFURA_PROJECT_ID=<your infura project id>
brownie console --network mainnet
```

inside the brownie console verify the connection to the network

```bash
>>> network.show_active()
'mainnet'
```

convert the address to a checksummed address (required by brownie) and check for its balance.
finally, quit the console using exit.

```bash
>>> addr = web3.toChecksumAddress('0x00000000219ab540356cbb839cbe05303d7705fa')
>>> print('{:,.5f} ETH'.format(web3.fromWei(web3.eth.getBalance(addr), "ether")))
8,318,914.00007 ETH
>>> exit()
```
