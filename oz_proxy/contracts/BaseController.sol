// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/proxy/utils/Initializable.sol";


contract BaseController is Initializable {

    uint256 public constant VERSION_V1 = 1;

    // must not use any initializer value here
    uint256 private _version;

    // modifier for version managment of upgrades
    modifier upgradeToVersion(uint256 newVersion) {
        require(newVersion == _version + 1, "BaseController: bad version");
        _version = newVersion;
        _;
    }

    // constructor logic implemented in initializer function for 
    // upgradable contracts
    function initialize() public virtual initializer {
        _version = VERSION_V1;
        _postInitialize();
    }

    // allows this function to be overridden by child contracts
    function version() public view returns (uint256) { return _version; }

    // initialization hook for child contracts
    function _postInitialize() internal virtual onlyInitializing {}
}
