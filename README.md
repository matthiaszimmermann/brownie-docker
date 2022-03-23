# brownie-docker
docker based brownie development

## links

* tutorial on [medium](https://iamdefinitelyahuman.medium.com/getting-started-with-brownie-part-1-9b2181f4cb99)
* working with [accounts](https://eth-brownie.readthedocs.io/en/stable/account-management.html)
* working with [networks](https://eth-brownie.readthedocs.io/en/stable/network-management.html)
* brownie [github](https://github.com/eth-brownie/brownie)
* chainlink's [install guide](https://chain.link/bootcamp/brownie-setup-instructions)

## clone the repo

before you execute any of the commands shown below clone this repository.

```bash
git clone https://github.com/matthiaszimmermann/brownie-docker.git
cd brownie-docker
```

## build the docker image

docker file based on brownie's [Dockerfile](https://github.com/eth-brownie/brownie/blob/master/Dockerfile), and corresponding requirements.txt

build the docker image

```bash
docker build -t brownie .
```

## setup of a new brownie project

using offline tx as example
```bash
mkdir offline_tx
cd offline_tx
docker run -it --rm -v $PWD:/projects brownie
```

inside the brownie container
```bash
brownie init
echo "# experimenting with offline tx signing" > README.md
```

in the ide write some contract eg `Ping.sol` in this case and compile the project 
```bash
brownie compile
```

use brownie console to deploy and interact with a Ping contract.

first start the console
```bash
brownie console
```

then, create a contract instance and show the address of the deployed contract
```bash
pingContract = Ping.deploy({'from': accounts[0]})
pingContract.address
```

and call the contracts ping method. use `tx.info()` to introspect the transaction returned by the contract call.
to exit the brownie console use `exit()`.

```bash
tx = pingContract.ping(42, {'from': accounts[1]})
tx.info()

exit()
```

use brownie testing.

in folder `tests` add file `conftest.py` to provide test fixtures that represent the application under test.
in this case method `pingContract` provides a deployed Ping contract.
this fixture is then used in `test_ping.py` for 3 simple test cases.
important: test case methods names need to start with prefix `test_` and parameters representing text fixtures need to mach with method names in  `conftest.py`.

with all that in place run the 3 test cases
```bash
brownie test
```

## run docker container

run docker container in interactive mode

```bash
docker run -it --rm \
    -v $PWD/accounts:/accounts \
    -v $PWD/brownie:/projects/brownie \
    -v $PWD/helloworld:/projects/helloworld \
    brownie
```

inside the container you can now work with brownie.

## use brownie image to start local ganache

As the brownie image contains an embedded [Ganache](https://trufflesuite.com/ganache/index.html) chain we can also use this image to create Ganache container as shown below.

```bash
docker run -d -p 7545:7545 --name ganache brownie ganache-cli \
    --mnemonic "candy maple cake sugar pudding cream honey rich smooth crumble sweet treat" \
    --chainId 1234 \
    --port 7545 \
    -h "0.0.0.0"

```

### ganache chain setup considerations
The chosen setup deterministically creates addresses (and private keys) via a HD wallet with the mnemonic `"candy maple cake sugar pudding cream honey rich smooth crumble sweet treat"`.
Port `7545` is chosen to avoid conflicts with any productive local ethereum client that typically run on port 8545.

## use metamask to connect to this chain

To connect with Metamaks using the mnemonic as secret recovery phrase.
As network parameter use `http://localhost:7545` as RPC URL and `1234` as Chain ID.

## use brownie console to connect to this chain


In the Brownie container add the ganache chain to the networks available to Brownie (see Brownie [Network Managment](https://eth-brownie.readthedocs.io/en/stable/network-management.html) for details about brownie networks).
Then, start Brownie console that connects to this chain.

```bash
brownie networks add Local ganache host=http://host.docker.internal:7545 chainid=1234
brownie console --network ganache
```

brownie recognizes the network and provides access to its accounts. 
the commands below show that brownie is connected to the local ganache chain and lists all inital accounts and balances.
```bash
print('network {} is_connected {}'.format(network.show_active(), network.is_connected()))
print('\n'.join(['{} {:.4f} ETH'.format(acc.address, Wei(acc.balance()).to('ether')) for acc in accounts]))
```

an account may also be directly created from a seed phrase
```bash
myAccount = accounts.from_mnemonic('candy maple cake sugar pudding cream honey rich smooth crumble sweet treat')
```

## use brownie with polygon, ...

start brownie container.

```bash
docker run -it --rm -v $PWD:/projects brownie
```

in the container list the networks available to brownie
```bash
brownie networks list
```

which prints network details to the console
```bash
...

Optimistic Ethereum
  ├─Mainnet: optimism-main
  └─Kovan: optimism-test

Polygon
  ├─Mainnet (Infura): polygon-main
  └─Mumbai Testnet (Infura): polygon-test

XDai
  ├─Mainnet: xdai-main
  └─Testnet: xdai-test
...
```

when we'd like to work with the polygon mumbai network `Mumbai Testnet (Infura): polygon-test` we need to specify our infura project id via environment variable before we can launch the brownie console.

```bash
export WEB3_INFURA_PROJECT_ID=<your infura project id here>
brownie console --network polygon-test
```

inside the console, we obtain an account via `accounts.add()`.
the shown mnemonic can be used to recreate the account at a later time.
```bash
>>> account = accounts.add()
mnemonic: 'depend bubble soccer depart pepper oblige royal coach menu during essence gauge'
>>> account.address
'0xf566aB4bb6e4ba6C4ABbeb183dbe1d5d96b9e337'
>>> Wei(acc.account()).to('ether')
Fixed('0E-18')
```

IMPORTANT make sure to safely store the mnemonic words for later use.
these words represent the private key to your account.
loosing these words is like loosing your money.
sharing these words is like handing over your money.

```bash
accountRecreated = accounts.from_mnemonic('<mnemonic words here>')
```

this account is initially empty and we need to transfer some funds to it before it can be used.
on test networks such as polygon-test public faucets are usually avaliable to obtain test 'money'.

the table below provides links to such test faucets and block explorers for test networks.

| name | brownie network id | | |
| -- | --- | -- | -- |
| gnosis | xdai-test | [faucet](https://faucet.poa.network/) | [explorer](https://blockscout.com/xdai/testnet)
| polygon | polygon-test | [faucet](https://faucet.polygon.technology/) | [explorer](https://mumbai.polygonscan.com/)
| avalanche | avax-test | [faucet](https://faucet.avax-test.network/) | [explorer](https://testnet.snowtrace.io) 
| binance smart chain | bsc-test | [faucet](https://testnet.binance.org/faucet-smart) | [explorer](https://testnet.bscscan.com/)

## use brownie

### work with the integrated ganache chain

the default for brownie console is to work with ganache.
to start the brownie console with the integrated ganache chain use the following command.

```bash
brownie console
```

this setup comes with 10 preloaded accounts that can be explored in the brownie console as shown below.

```bash
>>> len(accounts)
10
>>> dir(accounts[0])
[address, balance, deploy, estimate_gas, gas_used, get_deployment_address, nonce, transfer]
>>> print('{} {:.3f} ETH'.format(accounts[0].address, web3.fromWei(accounts[0].balance(), 'ether')))
0x66aB6D9362d4F35596279692F0251Db635165871 100.000 ETH
```

### compile and test a simple contract

a sample brownie project is provided in folder `helloworld`.
the project contains the contract `contracts/Box.sol`, corresponding test cases
and a deployment script.

the box contract makes use of the [`Ownable.sol`](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.3/contracts/access/Ownable.sol) contract from the OpenZeppelin library.
to use such external libraries they need to be installed in the brownie package manager. 
in addition, a remapping of the package location to the "standard" `@`-notation needs to be defined in `brownie-config.yaml`.

in order to compile the box contract use the command sequence shown below.
this step will create a number of book keeping files located in folder `build`.

```bash
cd helloworld
brownie pm install OpenZeppelin/openzeppelin-contracts@4.3.3
brownie compile
```

after successful compilation of the box contract execute the unit tests in folder `tests` and have brownie create code coverage reports that will be located in folder `reports`.

```bash
brownie test -C
```

for the tests the box contract is actually deployed to the local ganache chain.
the deployment step for this is implementd in the form of a test fixture in `tests/conftest.py`.
the files `tests/test_*.py` represent the contract unit tests that use these fixtures implicitly.

the code coverage results can then be viewed in the brownie gui.


```bash
brownie gui
```

to show the highlighted source code follow these steps

1. select contract `Box` in the top right drop down box
1. select report `coverage` in the drop down box to the left
1. select report type `branches` or `statements`

### deploy a simple contract

to deploy a contract to a chain you need to have a deployment account with sufficient funding to pay for the gas costs of deployment.

brownie's account handling allows to manage accounts via id that are linked to keystore files (see below for the creation of local accounts with keystores).

it is highly recommended to protect keystore files with passwords and keep keystore files outside any repository.
this prevents unitentional uploading of account credentials in any form. 
for the example below we assume that a keystore file `/accounts/deploy_account.json`
is available.

```bash
brownie accounts import deploy_account /accounts/deploy_account.json
brownie accounts list
```

you can now deploy the box contract as shown below. 

```bash
brownie run deploy
```
the `run <name>` command scans folder `scripts`, locates file `scripts/<name>.py` and executes its `main()` method


### connect to mainnet

as an example check the balance of a [example mainnet address](https://etherscan.io/address/0x00000000219ab540356cbb839cbe05303d7705fa) with a large amount of ethers.

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

### connect to xdai

brownie supports access to various networks out of the box.
use the command below to check for supported networks.

```bash
brownie networks list
```

[xdai](https://www.xdaichain.com/) is a evm blockchain designed for fast and inexpensive transactions. its token xdai is linked to the us dollar where 1 xdai = 1 us dollar.
to use brownie with xdai use.

```bash
brownie console --network xdai-main
```

inside the console 

```bash
>>> network.show_active()
'xdai-main'
>>> addr = web3.toChecksumAddress('0x00000000219ab540356cbb839cbe05303d7705fa')
>>> print('{:,.5f} DAI'.format(web3.fromWei(web3.eth.getBalance(addr), "ether")))
0.01000 DAI
```

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
see [ethereum wiki](https://github.com/ethereum/wiki/wiki/Web3-Secret-Storage-Definition) or [stackoverflow](https://ethereum.stackexchange.com/questions/37150/ethereum-wallet-v3-format) for more info regarding keystore files.
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

### brownie tests

to explore and verify brownie for various use cases corresponding unit tests are available in directory `brownie` of this repository.

these tests can be executed from within a running brownie container as shown below.

```bash
cd brownie
pytest
```

## openzeppelin access controls example

see the readme in folder `oz_access_control`

## swiss crypto stamps experiment

```bash
docker run -it --rm \
    -v $PWD/swiss_crypto_stamps:/projects \
    brownie
```

inside the brownie container (see brownie docs about [using infura](https://eth-brownie.readthedocs.io/en/stable/network-management.html))

```bash
export WEB3_INFURA_PROJECT_ID=<YourProjectID>
brownie run --network=polygon-main check_matterhorn
```

creates output

```bash
Brownie v1.17.1 - Python development framework for Ethereum

SwissCryptoStampsProject is the active project.

Running 'scripts/check_matterhorn.py::main'...
current network: polygon-main
proxy.totalSupply(1): 65000
proxy.totalSupply(2): 45000
proxy.totalSupply(3): 30000
proxy.totalSupply(4): 18000
proxy.totalSupply(5): 8000
proxy.totalSupply(6): 4500
proxy.totalSupply(7): 2500
proxy.totalSupply(8): 1000
proxy.totalSupply(9): 350
proxy.totalSupply(10): 250
proxy.totalSupply(11): 200
proxy.totalSupply(12): 150
proxy.totalSupply(13): 50
sample stamp account: 0xf3e3d5412aad4172e4d1fd39e7f912a11f2f0cbd
proxy.balanceOf(0xf3e3d5412aad4172e4d1fd39e7f912a11f2f0cbd, 1): 1
```
