import inspect
from nav.mibs.dlink_dgs_1210_xx import _DLink_DGS_1210_XX_Mib
from nav.smidumps import get_mib


class DLink_DGS_1210_12_TS_ME_BX_Mib(_DLink_DGS_1210_XX_Mib):
    mib = get_mib('D_Link_DGS_1210_12TSME_BX_7_03_001_mib')

    def _get_system_poe_sensors(self):
        self._logger.debug(here(self))
        return []


here = lambda this : '{}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
