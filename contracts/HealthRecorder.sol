pragma solidity ^0.4.18;

contract HealthRecorder
{
	mapping (address => bytes) healthRecords;

	function setRecord(address patient, bytes recordCipherText) public
	{
		healthRecords[patient] = recordCipherText;
	}

	function getRecord(address patient) public constant returns(bytes)
	{
		return healthRecords[patient];
	}
}