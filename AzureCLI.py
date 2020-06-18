import azure.mgmt.compute as Compute
from azure.common.client_factory import get_client_from_cli_profile
import logging
import json


class AzureCLI:

    def listVMs():
        try:
            VM = get_client_from_cli_profile(Compute.ComputeManagementClient)
            listVMs = VM.virtual_machines.list_all()

            for i in listVMs:
                string = str(i)
                js = json.dumps(string)
                return json.loads(js)

        except Exception as e:
            logging.error(msg=e)
