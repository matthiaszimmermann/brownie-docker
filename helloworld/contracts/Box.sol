pragma solidity ^0.8.0;

// SPDX-License-Identifier: Apache-2.0

// brownie pm install OpenZeppelin/openzeppelin-contracts@4.3.3
// for actual source see https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.3/contracts/access/Ownable.sol
// see brownie-config.yaml for the mapping from '@openzeppelin' to the actual package
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 *  @dev simple counter contract
 */
contract Box is Ownable {
    uint256 private _value;

    /**
     *  @dev indicates that box value has changed
     */
    event ValueChanged(uint256 value);

    /**
     *  @dev sets new box value
     *  only owner is allowed to change box value
     */
    function store(uint256 value) public onlyOwner {
        _value = value;
        emit ValueChanged(_value);
    }

    /**
     *  @dev increase box value if below 100
     */
    function inc() public {
        if(_value < 100) {
            _value += 1;
            emit ValueChanged(_value);
        }
    }

    /**
     *  @dev returns current box value
     */
    function retrieve() public view returns (uint256) {
        return _value;
    }   
}
