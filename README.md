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
docker run -it --rm brownie
```

inside the container you can now work with brownie.

## use brownie

as an initial example check the balance of an mainnet address with a large amount of ethers.
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
