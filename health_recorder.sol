pragma ^0.4.19

contract HealthRecorder
{
	mapping (address => bytes) healthRecords

	function HealthRecorder() {}

	function setRecord(address patient, bytes recordCipherText) public
	{
		healthRecords[patient] = recordCipherText;
	}

	function getRecord(address patient) returns(bytes) public
	{
		return healthRecords[patient];
	}
}