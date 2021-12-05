
starting via swiss.post.ch

https://crypto-stamp.post.ch/en/questions-and-answers
"what is a smart contract"
-> source address that crated swiss crypto stamp contracts
https://polygonscan.com/address/0x97ebe3fe2feb21ba8f99d99e8275a8c4d5066fc2

contract creation tx
https://polygonscan.com/tx/0xbf18dbc87b33b7cadf15e0114c16b4913546210fe1c9ca33a00cdb03a5159528
- contract 1 https://polygonscan.com/tx/0xbf18dbc87b33b7cadf15e0114c16b4913546210fe1c9ca33a00cdb03a5159528
  + contract https://polygonscan.com/address/0xbd481f5345f41aaeaac2a72f0ae22fab89f170d2#code
    * "CryptoStampPolygon"
      > CryptoStampPolygon is CryptoStamp
      > CryptoStamp is Initializable, OwnableUpgradeable, ERC1155SupplyUpgradeable
      > ERC1155SupplyUpgradeable is Initializable, ERC1155Upgradeable
      > ERC1155Upgradeable is Initializable, ContextUpgradeable, ERC165Upgradeable, IERC1155Upgradeable, IERC1155MetadataURIUpgradeable
        = function balanceOf(address account, uint256 id) public view virtual override returns (uint256) {
        = function safeTransferFrom(address from, address to, uint256 id, uint256 amount, bytes memory data)

- contract 2 https://polygonscan.com/tx/0xf0d9b77f457627801efeff19bdc50937f2efeaefb9eaa0874a64cb3d8639befd
  + contract https://polygonscan.com/address/0xdd29d0792bb78b46d187cc8d3efdd8d71f4c3379#code
    * "AdminUpgradeabilityProxy"
      > AdminUpgradeabilityProxy is TransparentUpgradeableProxy
      > TransparentUpgradeableProxy is ERC1967Proxy
      > ERC1967Proxy is Proxy, ERC1967Upgrade

- contract 3 https://polygonscan.com/tx/0x0c99af9c69dbb3cf454d165fa5bf0624700c64343d8a2cf243689458876cc68c
  + contract https://polygonscan.com/address/0x6ddcc90614d47acd7596447686c4fd6aee782742#code
    > looks very much like contract2 but flattened (no imports)
    > TransparentUpgradeableProxy is ERC1967Proxy
      = constructor takes implementation as argument, emits log
      = upgradeTo(address newImplementation) external ifAdmin
      = upgradeToAndCall(address newImplementation, bytes calldata data) external payable ifAdmin
        => emit Upgraded(newImplementation);
           https://polygonscan.com/tx/0x0c99af9c69dbb3cf454d165fa5bf0624700c64343d8a2cf243689458876cc68c#eventlog
           Transaction Receipt Event Logs
           Address
               0x6ddcc90614d47acd7596447686c4fd6aee782742
           Name
               Upgraded (index_topic_1 address implementation)
           Topics
               0 0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b (hash of signature of event, =upgraded in this case)
               1 0xbd481f5345f41aaeaac2a72f0ae22fab89f170d2 (= crypto stamp polygon contract address from above)
      
      = checking all events of type upgraded for contract shows that event from contract creation tx was only one

starting from open sea
https://opensea.io/collection/swiss-crypto-stamp
https://opensea.io/assets/matic/0x6ddcc90614d47acd7596447686c4fd6aee782742/1
Contract Address: 0x6ddc...2742 -> https://polygonscan.com/address/0x6ddcc90614d47acd7596447686c4fd6aee782742
  ==> this is the TransparentUpgradeableProxy from above :-)
Token ID: 1
Token Standard: ERC-1155
Blockchain: Polygon
