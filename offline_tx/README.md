# experimenting with offline tx signing

## setup

simple `Ping` contract. start brownie container to deploy and use contract

```bash
cp .env.demo .env
docker run -it --rm -v $PWD:/projects brownie
```

compile contract and start brownie console
```bash
brownie compile
brownie console
```

inside the console, create a contract instance and show the address of the deployed contract
```bash
pingContract = Ping.deploy({'from': accounts[0]})
pingContract.address
```

call the contracts `ping` method. use `tx.info()` to introspect the transaction returned by the contract call.

```bash
tx = pingContract.ping(42, {'from': accounts[1]})
tx.info()
```

the info method should provide output similar to the one provided below.
```bash
Transaction sent: 0xa3a6589539c065bfbe2b77a147ccd3772ba5f4ff188abfe1a54e547c99762113
  Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
  Ping.ping confirmed   Block: 2   Gas used: 65338 (0.54%)

>>> tx.info()
Transaction was Mined
---------------------
Tx Hash: 0xa3a6589539c065bfbe2b77a147ccd3772ba5f4ff188abfe1a54e547c99762113
From: 0x33A4622B82D4c04a53e170c638B944ce27cffce3
To: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87
Value: 0
Function: Ping.ping
Block: 2
Gas Used: 65338 / 12000000 (0.5%)

Events In This Transaction
--------------------------
└── Ping (0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87)
    └── LogPinged
        ├── number: 42
        └── pings: 1
```

## offline transaction handling

offlie transaction handling demonstrated in the form of unit tests.
see `tests/test_ping_offline.py` method `test_ping_offline`.

the general mechanism is as follows.

1. a web3 library contract instance is created
2. the web3 library method `buildTransaction` is used to create an unsigned transaction
3. the unsigned transaction is amended with the current nonce of the sending account
4. the private key of the sending account is used to sign the transaction
5. the signed transaction is sent to the network

module `scripts/util.py` provides simple utility methods for steps 1. (`get_web3_contract`), 3/4 (`get_signed_transaction`) and 5 (`submit_signed_transaction`).

use brownie test to run the offline signing unit test.

```bash
brownie test -v
```
