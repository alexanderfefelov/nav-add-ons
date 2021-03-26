from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class Extreme_Networks_Software_Monitor_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('Extreme_Networks_EXTREME_SOFTWARE_MONITOR_MIB_mib')
    GUARD_OID = 'extremeSwMonitor'

    @defer.inlineCallbacks
    def get_cpu_loadavg(self):
        self._logger.debug(here(self))
        result = {}
        columns = yield self.retrieve_columns([
            'extremeCpuMonitorSystemSlotId',
            'extremeCpuMonitorSystemUtilization1min',
            'extremeCpuMonitorSystemUtilization5mins'
        ])
        if columns:
            for _, item in columns.items():
                slot_id = item.get('extremeCpuMonitorSystemSlotId')
                slot_name = 'slot_%d' % slot_id
                utilization_1_min = item.get('extremeCpuMonitorSystemUtilization1min')
                utilization_5_min = item.get('extremeCpuMonitorSystemUtilization5mins')
                result[slot_name] = [
                    (1, utilization_1_min),
                    (5, utilization_5_min)
                ]
        defer.returnValue(result)

    def get_cpu_utilization(self):
        self._logger.debug(here(self))
        return defer.succeed(None)

    @defer.inlineCallbacks
    def get_memory_usage(self):
        self._logger.debug(here(self))
        result = {}
        columns = yield self.retrieve_columns([
            'extremeMemoryMonitorSystemSlotId',
            'extremeMemoryMonitorSystemTotal',
            'extremeMemoryMonitorSystemFree'
        ])
        if columns:
            for _, item in columns.items():
                slot_id = item.get('extremeMemoryMonitorSystemSlotId')
                slot_name = 'slot_%d' % slot_id
                total = int(item.get('extremeMemoryMonitorSystemTotal')) * 1024
                free = int(item.get('extremeMemoryMonitorSystemFree')) * 1024
                used = total - free
                result[slot_name] = (used, free)
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
