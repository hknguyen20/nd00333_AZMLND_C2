from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Requires the config to be downloaded first to the current working directory
session_id = "268650"
subscription_id= "aa7cf8e8-d23f-4bce-a7b9-1f0b4e0ac8ee"
resource_group= f"aml-quickstarts-{session_id}"
workspace_name= f"quick-starts-ws-{session_id}"

ws = Workspace.get(name=workspace_name, subscription_id=subscription_id, resource_group=resource_group)
# Set with the deployment name
name = ""

# load existing web service
service = Webservice(name=name, workspace=ws)
logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
