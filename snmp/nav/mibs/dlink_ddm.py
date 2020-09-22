from nav.mibs.dlink import DLink
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
import inspect


class DLink_Ddm_Mib(MibRetriever, DLink):
    mib = get_mib('D_Link_DDM_mib')
    SUPPORTED_ROOT = 'swDdmMIB'

    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        return self._get_ddm_sensors_old()


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
