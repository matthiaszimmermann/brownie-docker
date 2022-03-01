// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

import "./CounterControllerV1.sol";

contract CounterControllerV2 is CounterControllerV1 {

    // controller version number
    uint256 public constant VERSION_V2 = 2;

    // state for previous value of counter
    uint256 private _previousValue;

    // additional business logic for this version
    function previousValue() public view returns (uint256) { 
        return _previousValue; 
    }   

    // upgrade/migration of contract state to setup for new version
    // introduction of new state variable that depends on current state
    // necessary migration/initialisation in implemetation body
    function upgradeToV2(uint256 value) external upgradeToVersion(VERSION_V2) {
        _previousValue = CounterControllerV1.value();
        _setValue(value);
    }

    function _setValue(uint256 newValue) internal override { 
        _previousValue = value();
        CounterControllerV1._setValue(newValue);
    }
}
