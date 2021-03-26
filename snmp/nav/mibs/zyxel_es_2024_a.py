from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class ZyXEL_ES_2024_A_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('ZyXEL_390TX3C0_mib')

    def get_cpu_loadavg(self):
        self._logger.debug(here(self))
        return defer.succeed(None)

    @defer.inlineCallbacks
    def get_cpu_utilization(self):
        self._logger.debug(here(self))
        result = {}
        utilization = yield self.get_next('sysMgmtCPUUsage')
        result['cpu'] = utilization
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_memory_usage(self):
        self._logger.debug(here(self))
        result = {}
        columns = yield self.retrieve_columns([
            'sysMemoryPoolName',
            'sysMemoryPoolTotal',
            'sysMemoryPoolUsed'
        ])
        if columns:
            for _, item in columns.items():
                pool_name = item.get('sysMemoryPoolName')
                total = int(item.get('sysMemoryPoolTotal'))
                used = int(item.get('sysMemoryPoolUsed'))
                free = total - used
                result[str(pool_name)] = (used, free)
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
