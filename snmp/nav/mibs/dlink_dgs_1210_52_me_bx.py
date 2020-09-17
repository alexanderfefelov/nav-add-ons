import inspect
from nav.mibs.dlink_dgs_1210_xx import _DLink_DGS_1210_XX_Mib
from nav.smidumps import get_mib


class DLink_DGS_1210_52_ME_BX_Mib(_DLink_DGS_1210_XX_Mib):
    mib = get_mib('D_Link_DGS_1210_52ME_BX_7_02_017_mib')

    def _get_ports_poe_columns(self):
        self._logger.debug(here(self))
        return []

    def _get_ports_poe_sensors(self, data):
        self._logger.debug(here(self))
        return []

    def _get_system_poe_sensors(self):
        self._logger.debug(here(self))
        return []


here = lambda this : 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
