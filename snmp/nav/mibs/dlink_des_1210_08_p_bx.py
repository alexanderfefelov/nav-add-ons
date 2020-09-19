from nav.mibs.dlink_des_1210_xx import DLink_DES_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
import inspect


class DLink_DES_1210_08_P_BX_Mib(MibRetriever, DLink_DES_1210_XX):
    mib = get_mib('D_Link_DES_1210_08P_BX_v3_12_004_mib')
    SUPPORTED_ROOT = 'des-1210-08p-bx'

    def get_ports_poe_sensors(self):
        self._logger.debug(here(self))
        return self._get_ports_poe_sensors()

    def get_system_poe_sensors(self):
        self._logger.debug(here(self))
        return self._get_system_poe_sensors()


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
