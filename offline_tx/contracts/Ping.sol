// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;


contract Ping {

    uint256 private _pings;
    uint256 private _pingSum;

    event LogPinged(uint256 number, uint256 pings);

    function ping(uint256 number) public payable {
        _pingSum += number;
        _pings += 1;

        emit LogPinged(number, _pings);
    }

    function pings() public view returns (uint256) { return _pings; }
    function pingSum() public view returns (uint256) { return _pingSum; }
}
