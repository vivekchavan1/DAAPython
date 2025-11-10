// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {
    address public accHolder;

    constructor() {
        accHolder = msg.sender;
    }

    function withdraw(uint256 amount) public {
        require(msg.sender == accHolder, "You are not the account holder");
        require(amount > 0, "Withdraw amount should be greater than 0");
        require(amount <= address(this).balance, "Insufficient balance in contract");

        payable(msg.sender).transfer(amount);
    }

    function deposite() public payable {
        require(msg.sender == accHolder, "You are not the account holder");
        require(msg.value > 0, "Deposit amount should be greater than 0");
        // Ether automatically added to contract balance
    }

    function showBalance() public view returns (uint256) {
        require(msg.sender == accHolder, "You are not the account owner.");
        return address(this).balance;
    }
}
