from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class DLink_DGS_1210_10_P_ME_BX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_10PME_BX_7_02_017_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        ddm_sensors = yield self.get_ddm_sensors()
        ports_poe_sensors = yield self.get_ports_poe_sensors()
        system_poe_sensors = yield self.get_system_poe_sensors()
        result.extend(ddm_sensors)
        result.extend(ports_poe_sensors)
        result.extend(system_poe_sensors)
        self._logger.debug(str(result))
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
