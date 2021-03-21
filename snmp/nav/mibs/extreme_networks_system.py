from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class Extreme_Networks_System_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('Extreme_Networks_EXTREME_SYSTEM_MIB_mib')
    GUARD_OID = 'extremeSystem'

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        fan_sensors = yield self._get_fan_sensors()
        result.extend(fan_sensors)
        power_sensors = yield self._get_power_sensors()
        result.extend(power_sensors)
        temperature_sensors = yield self._get_temperature_sensors()
        result.extend(temperature_sensors)
        self._logger.info('%d sensor(s) detected', len(result))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def _get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'extremeFanNumber',
            'extremeFanOperational',
            'extremeFanSpeed'
        ])
        if columns:
            for _, item in columns.items():
                index = item.get('extremeFanNumber')
                result.append(self.get_indexed_system_sensor(index, 'extremeFanOperational', ''))
                result.append(self.get_indexed_system_sensor(index, 'extremeFanSpeed', Sensor.UNIT_RPM))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def _get_power_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'extremePowerSupplyNumber',
            'extremePowerSupplyInputVoltage',
            'extremePowerSupplyFan1Speed',
            'extremePowerSupplyFan2Speed',
            'extremePowerSupplyInputPowerUsage'
        ])
        if columns:
            for _, item in columns.items():
                index = item.get('extremePowerSupplyNumber')
                result.append(self.get_indexed_system_sensor(index, 'extremePowerSupplyInputVoltage', ''))
                result.append(self.get_indexed_system_sensor(index, 'extremePowerSupplyFan1Speed', Sensor.UNIT_RPM))
                result.append(self.get_indexed_system_sensor(index, 'extremePowerSupplyFan2Speed', Sensor.UNIT_RPM))
                result.append(self.get_indexed_system_sensor(index, 'extremePowerSupplyInputPowerUsage', Sensor.UNIT_WATTS))  # FIXME precision?
        defer.returnValue(result)

    def _get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('extremeCurrentTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
