import os
import logging


class AzureCLI:

    def listVMs():
        try:
            az = os.system('az vm list')
            return az

        except Exception as e:
            logging.error(msg=e)