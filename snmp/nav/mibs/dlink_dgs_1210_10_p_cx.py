from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
import inspect


class DLink_DGS_1210_10_P_CX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_10P_CX_4_10_002_mib')
    SUPPORTED_ROOT = 'dgs-1210-10pcx'

    def get_ports_poe_sensors(self):
        self._logger.debug(here(self))
        return self._get_ports_poe_sensors()

    def get_system_poe_sensors(self):
        self._logger.debug(here(self))
        return self._get_system_poe_sensors()


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
