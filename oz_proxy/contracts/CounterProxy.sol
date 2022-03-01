// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/proxy/transparent/TransparentUpgradeableProxy.sol";

contract CounterProxy is TransparentUpgradeableProxy { 

    constructor(address _logic, bytes memory encoded_initializer)
        TransparentUpgradeableProxy(_logic, msg.sender, encoded_initializer) 
    {}
}
