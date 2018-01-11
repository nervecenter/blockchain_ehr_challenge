from populus.project import Project

p = Project()
with p.get_chain('emr') as chain:
    health_recorder, deploy_tx_hash = chain.provider.get_or_deploy_contract('HealthRecorder')

print("Health Recorder contract address on emr is {address}".format(address=health_recorder.address))
if deploy_tx_hash is None:
    print("The contract is already deployed on the chain")
else:
    print("Deploy Transaction {tx}".format(tx=deploy_tx_hash))