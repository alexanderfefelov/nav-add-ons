from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
import inspect


class DLink_DGS_1210_10_ME_AX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_10ME_AX_6_14_001_mib')
    SUPPORTED_ROOT = 'dgs-1210-10meax'

    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        return self._get_ddm_sensors()


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
