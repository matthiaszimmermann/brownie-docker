# OpenZeppelin TransparentUpgradeableProxy Contract

OpenZeppelin [Proxies](https://docs.openzeppelin.com/contracts/4.x/api/proxy) allows to implement upgradable smart contracts.

## Writing upgradable Contracts

[Official OpenZeppelin Intro](https://docs.openzeppelin.com/upgrades-plugins/1.x/writing-upgradeable)

## Example Setup

* UpgradableCounter (proxie + storage)
* BaseController (plumbing for upgradable version management)
* CounterControllerV1 (initial logic implementation)
* CounterControllerV2 (upgraded logic implementation)

## Run the Tests Cases

Experimenting with Open Zeppelins proxy contracts is implemented as brownie tests against the sample contract.

Create a running Docker container

```bash
docker run -it --rm -v $PWD/oz_proxy:/projects brownie
```

And inside the Docker container

```bash
brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0
brownie compile
brownie test
```