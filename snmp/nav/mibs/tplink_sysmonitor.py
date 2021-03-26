from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class TPLink_Sysmonitor_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('TP_Link_tplink_sysMonitor_mib')

    @defer.inlineCallbacks
    def get_cpu_loadavg(self):
        self._logger.debug(here(self))
        result = {}
        columns = yield self.retrieve_columns([
            'tpSysMonitorCpuUnitNumber',
            'tpSysMonitorCpu1Minute',
            'tpSysMonitorCpu5Minutes'
        ])
        if columns:
            for _, item in columns.items():
                unit_no = item.get('tpSysMonitorCpuUnitNumber')
                unit_name = 'unit_%d' % unit_no
                utilization_1_min = item.get('tpSysMonitorCpu1Minute')
                utilization_5_min = item.get('tpSysMonitorCpu5Minutes')
                result[unit_name] = [
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
            'tpSysMonitorMemoryUnitNumber',
            'tpSysMonitorMemoryUtilization'
        ])
        if columns:
            for _, item in columns.items():
                unit_no = item.get('tpSysMonitorMemoryUnitNumber')
                unit_name = 'unit_%d' % unit_no
                utilization = item.get('tpSysMonitorMemoryUtilization')
                free = 100 - utilization
                result[unit_name] = (utilization, free)
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
