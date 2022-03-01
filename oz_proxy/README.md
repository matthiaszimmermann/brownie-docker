# OpenZeppelin TransparentUpgradeableProxy Contract

OpenZeppelin [Proxies](https://docs.openzeppelin.com/contracts/4.x/api/proxy) allows to implement upgradable smart contracts.

## Writing upgradable Contracts

[Official OpenZeppelin Intro](https://docs.openzeppelin.com/upgrades-plugins/1.x/writing-upgradeable)

### Initializer

Controllers constructors are irrelevant for upgradable contracts. 
Reason: The proxy contract is holding the state of the smart contract, not the controller contract.

Therefore OpenZeppelin introduces the `Initializable` base contract with dome plumbing to properly initialize upgradable contracts and ensuring
that this initializer may only be called once (as for constructors).

Once an initializable contract has been deployed as the V1 of the upgradable contract the proxy's state no longer allows for any additional initialization.

### Upgrading and Migration of Contract State

What seems to be missing in the OpenZeppelin setup is some similar plumbing to manage/handle version upgrades of the controller contracts.

Contract `BaseController` tries to provide such minimal functionality.
A controller contract inheriting from this base contract carries a version number that represents the current version of an upgradable contract.
In addition, `BaseController` provides the modifier `upgradeToVersion`.
This modifier allows for an upgrade functions in new controller contract versions that ensures that replacement of controller logic is done from version 1 to 2,3,... without repetitions or gaps.

For some concrete controller logic upgrade examples see test cases `tests/test_upgrade_v2.py` and `tests/test_upgrade_v2.py`.

## Example Setup

* `CounterProxy` (proxie + storage)
* `BaseController` (plumbing for upgradable version management)
* `CounterControllerV1` (initial logic implementation, shows contract initialization)
* `CounterControllerV2` (upgraded logic implementation to hold previous value of counter, shows contract state upgrade)
* `CounterControllerV3` (upgraded logic adds dec() functionality)

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