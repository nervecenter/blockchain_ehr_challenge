pragma ^0.4.19

contract Registry
{
    struct Doctor
    {
    	string hospital;
    	string expertise;
    }

    mapping (address => Doctor) doctors;

	struct Patient
	{
		bytes publicKey;
	}

	mapping (address => Patient) patients;

	function Registry()
	{

	}

	function addDoctor(string hospital, string expertise)