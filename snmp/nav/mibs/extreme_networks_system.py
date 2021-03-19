from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class Extreme_Networks_System_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('Extreme_Networks_EXTREME_SYSTEM_MIB_mib')
    ROOT_OID = 'extremeSystem'

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        fan_sensors = yield self._get_fan_sensors()
        result.extend(fan_sensors)
        self._logger.info('%d sensor(s) detected', len(result))
        defer.returnValue(result)

    def _get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
