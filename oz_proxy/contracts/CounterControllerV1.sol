// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

import "./BaseController.sol";


contract CounterControllerV1 is BaseController {

    uint256 public constant INITIAL_VALUE = 100;

    // state variable for current value of counter
    uint256 private _value;

    // public functionality
    function inc() public { _setValue(_value + 1); }
    function value() public view returns (uint256) { return _value; }

    // internal functions
    function _setValue(uint256 newValue) internal virtual { _value = newValue; }

    function _postInitialize() internal override onlyInitializing {
         _setValue(INITIAL_VALUE);
    }
}
