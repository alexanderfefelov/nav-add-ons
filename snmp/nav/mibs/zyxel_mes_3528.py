from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class ZyXEL_MES_3528_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('ZyXEL_390BHR5C0_mib')

    def get_cpu_loadavg(self):
        self._logger.debug(here(self))
        return None

    @defer.inlineCallbacks
    def get_cpu_utilization(self):
        self._logger.debug(here(self))
        result = {}
        utilization = yield self.get_next('sysMgmtCPUUsage')
        result['cpu'] = utilization
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
