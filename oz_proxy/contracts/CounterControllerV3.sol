// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

import "./CounterControllerV2.sol";

contract CounterControllerV3 is CounterControllerV2 {

    // controller version number
    uint256 public constant VERSION_V3 = 3;

    // additional business logic for this version
    function dec() public { _setValue(value() - 1); }

    // upgrade/migration of contract state to setup for new version
    // only new functionality, no state migration necessary
    // -> empty implementation body
    function upgradeToV3() external upgradeToVersion(VERSION_V3) {}
}
