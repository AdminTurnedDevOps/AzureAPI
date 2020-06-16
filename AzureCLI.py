from azure.cli.core import get_default_cli as azcli
import logging

class AzureCLI:

    def listVMs():
        try:
            cli = azcli().invoke('vm', 'list')
            return cli

        except Exception as e:
            logging.error(msg='The Azure CLI could not be contacted...')