from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from nav.smidumps import get_mib
import inspect


class DLink_DGS_1210_52_ME_BX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_52ME_BX_7_02_017_mib')
    SUPPORTED_ROOT = 'dgs-1210-52mebx'

    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        return self._get_ddm_sensors()

    def get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('sysSmartFanStatus', ''))
        return result

    def get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('sysTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
