// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";



contract FundMe {
    using SafeMathChainlink for uint256;

    mapping(address => uint256) public addressToAmountFunded;
    address[] public funderArray;
    address public owner;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function isFunderNew(address funder) public view returns (bool) {
        for(uint i=0; i < funderArray.length; i++) {
            if (funderArray[i] == funder) {
                return false;
            }
        }
        return true;
    }

    function fund() public payable {
        uint256 minimumUSD = 50 * 10**18;
        require(getConversionRate(msg.value) >= minimumUSD, "Don't be rata");
        addressToAmountFunded[msg.sender] += msg.value;
        if (isFunderNew(msg.sender)) {
            funderArray.push(msg.sender);
        }
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    function getDecimals() public view returns (uint8) {
        return priceFeed.decimals();
    }

    function getPrice() public view returns (uint256) {
        (,int256 price,,,) = priceFeed.latestRoundData();
        return uint256(price * (10**10));
    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256) {
        uint256 usdPrice = getPrice();
        uint256 ethToUSD = (ethAmount * usdPrice) / (10**18);
        return ethToUSD;
    }

    function getEntranceFee() public view returns (uint256) {
        uint256 minimumPriceUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (minimumPriceUSD * precision) / price;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function withdraw() public onlyOwner payable {
        msg.sender.transfer(address(this).balance);
        for(uint256 i=0; i < funderArray.length; i++) {
            addressToAmountFunded[funderArray[i]] = 0;
        }
        funderArray = new address[](0);
    }   
}
