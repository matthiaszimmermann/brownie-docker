# OpenZeppelin AccessControl Contract

OpenZeppelin [Access Control](https://docs.openzeppelin.com/contracts/4.x/access-control) allows to implement simple role based granting for smart contracts.

## Example Setup

Contract `ProtectedCounter` manages a integer value with contract functions `inc()` to increase and `dec()` decrese that value.
This sample contract inherits its granting functionality from Open Zeppelins [AccessControlEnumerable](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v4.5/contracts/access/AccessControlEnumerable.sol) contract which in turn inherits from [AccessControl](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v4.5/contracts/access/AccessControl.sol)

To call increse or decrease functions the calling account needs to have the appropriate roles `ADDER_ROLE` and `SUBTRACTER_ROLE` respectively.
Querying the integer value does not require any priviledges/roles.

The contract constructor grants the owner account the `DEFAULT_ADMIN_ROLE` defined in contract `AccessControl` and the `ADDER_ROLE` via `_setupRole()`.
Role `DEFAULT_ADMIN_ROLE` is the default role that is required to call method `grantRole()`.

Before granting a role to any account method `grantRole()` checks that the caller actually has assigned the `DEFAULT_ADMIN_ROLE`.
Using the contract internal method `_setRoleAdmin()` this granting permission may be transferred to another role.

In the example contract `ProtectedCounter` the role admin for role `ADDER_ROLE` is transferred from `DEFAULT_ADMIN_ROLE` to `ADDER_ROLE` itself.
This adds a form of "transitive" granting to the `ADDER_ROLE`.
Any account with the `ADDER_ROLE` can then grant the `ADDER_ROLE` to any other account.
This transfer of the role admin also means that the `DEFAULT_ADMIN_ROLE` is no longer able to grant `ADDER_ROLE` to any account.
Therefore the `ADDER_ROLE` needs to explicitly be provided to the contract creator account in the constructor as well.

## Run the Tests Cases

Experimenting with Open Zeppelins access control classis is implemented as brownie tests against the `ProtectedCounter` sample contract.

Create a running Docker container

```bash
docker run -it --rm -v $PWD/oz_access_control:/projects brownie
```

And inside the Docker container

```bash
brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0
brownie compile
brownie test
```