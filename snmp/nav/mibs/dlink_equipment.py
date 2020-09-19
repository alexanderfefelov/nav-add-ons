from nav.mibs.mibretriever import MibRetriever
from nav.mibs.dlink import DLink
from nav.smidumps import get_mib
import inspect


class DLink_Equipment_Mib(MibRetriever, DLink):
    mib = get_mib('D_Link_Equipment_mib')
    SUPPORTED_ROOT = 'swEquipmentMIB'

    def get_fan_sensors(self):
        self._logger.debug(here(self))
        return self._get_fan_sensors()

    def get_temperature_sensors(self):
        self._logger.debug(here(self))
        return self._get_temperature_sensors()


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
