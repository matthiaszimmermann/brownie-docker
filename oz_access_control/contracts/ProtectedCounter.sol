// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

// brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0
// for actual source see https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.3/contracts/access/Ownable.sol
// see brownie-config.yaml for the mapping from '@openzeppelin' to the actual package
import "@openzeppelin/contracts/access/AccessControlEnumerable.sol";


contract ProtectedCounter is AccessControlEnumerable {

    bytes32 public constant ADDER_ROLE = keccak256("ADDER_ROLE");
    bytes32 public constant SUBTRACTOR_ROLE = keccak256("SUBTRACTOR_ROLE");

    uint256 private constant INITIAL_VALUE = 100;
     
    uint256 private _value;

    constructor() {
        // assign contract creator admin and adder roles
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(ADDER_ROLE, msg.sender);

        // maker adder role transitive (= "with granting")
        // let account with role adder assign adder role to other accounts
        // ie once an account has the adder role it can assign the adder role to other accounts
        _setRoleAdmin(ADDER_ROLE, ADDER_ROLE);

        _value = INITIAL_VALUE;
    }

    function inc() public onlyRole(ADDER_ROLE) { _value += 1; }
    function dec() public onlyRole(SUBTRACTOR_ROLE) { _value -= 1; }
    function value() public view returns (uint256) { return _value; }   
}
