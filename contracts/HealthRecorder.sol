pragma solidity ^0.4.18;

contract HealthRecorder
{
	mapping (address => string) healthRecords;

	function setRecord(address patient, string recordCipherText) public
	{
		healthRecords[patient] = recordCipherText;
	}

	function getRecord(address patient) public constant returns(string)
	{
		return healthRecords[patient];
	}
}