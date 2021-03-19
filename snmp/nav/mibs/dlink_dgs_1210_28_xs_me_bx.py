from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
import inspect


class DLink_DGS_1210_28_XS_ME_BX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_28XSME_BX_7_03_001_mib')
    ROOT_OID = 'dgs-1210-28xsmebx'
    GET_DDM_SENSORS = 'get_ddm_sensors'
    GET_FAN_SENSORS = '_get_fan_sensors'

    def _get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('sysSmartFanStatus', ''))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
