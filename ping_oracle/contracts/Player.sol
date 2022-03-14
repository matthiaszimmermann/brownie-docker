// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

contract Player {

    string private _playerName;
    uint256 private _moves;
    Player private _opponent;

    event LogMove(string player, uint256 call, uint256 moves);

    constructor(string memory name) {
        _playerName = name;
    }

    function move(uint256 calls) public {
        if (calls > 0) {
            _moves += 1;

            emit LogMove(_playerName, calls, _moves);

            _opponent.move(calls - 1);
        }
    }

    function setOpponent(address player) public { _opponent = Player(player); }
    function moves() public view returns (uint256) { return _moves; }
}
