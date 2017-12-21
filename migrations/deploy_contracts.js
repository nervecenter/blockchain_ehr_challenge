var Migrations = artifacts.require("./Migrations.sol");
var HealthRecorder = artifacts.require("./health_recorder.sol");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(HealthRecorder);
};
