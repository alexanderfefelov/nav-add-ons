from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class NetPing_DKSF_60_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('NetPing_DKSF_60_5_2_MB_mib')
    GUARD_OID = 'lightcom'

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        temperature_sensors = yield self._get_temperature_sensors()
        result.extend(temperature_sensors)
        self._logger.info('%d sensor(s) detected', len(result))
        defer.returnValue(result)

    def _get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        for index in range(1, 9):
            result.append(self.get_indexed_system_sensor(index, 'npThermoStatus', ''))
            result.append(self.get_indexed_system_sensor(index, 'npThermoValue', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
            result.append(self.get_indexed_system_sensor(index, 'npThermoLow', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
            result.append(self.get_indexed_system_sensor(index, 'npThermoHigh', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
