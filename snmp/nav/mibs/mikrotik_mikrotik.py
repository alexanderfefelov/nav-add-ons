from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class MikroTik_Mikrotik_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('MikroTik_mikrotik_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        fan_sensors = yield self.get_fan_sensors()
        power_supply_sensors = yield self.get_power_supply_sensors()
        temperature_sensors = yield self.get_temperature_sensors()
        other_sensors = yield self.get_other_sensors()
        result.extend(fan_sensors)
        result.extend(power_supply_sensors)
        result.extend(temperature_sensors)
        result.extend(other_sensors)
        self._logger.debug(str(result))
        defer.returnValue(result)

    def get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('mtxrHlActiveFan', ''))
        result.append(self.get_system_sensor('mtxrHlFanSpeed1', Sensor.UNIT_RPM))
        result.append(self.get_system_sensor('mtxrHlFanSpeed2', Sensor.UNIT_RPM))
        return result

    def get_power_supply_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('mtxrHlBackupPowerSupplyState', ''))
        result.append(self.get_system_sensor('mtxrHlPowerSupplyState', ''))
        result.append(self.get_system_sensor('mtxrHlCurrent', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
        result.append(self.get_system_sensor('mtxrHlPower', Sensor.UNIT_WATTS, 1))
        result.append(self.get_system_sensor('mtxrHlCoreVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self.get_system_sensor('mtxrHlFiveVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self.get_system_sensor('mtxrHlThreeDotThreeVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self.get_system_sensor('mtxrHlTwelveVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self.get_system_sensor('mtxrHlVoltage', Sensor.UNIT_VOLTS_AC, maximum=300))
        return result

    def get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('mtxrHlBoardTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self.get_system_sensor('mtxrHlCpuTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self.get_system_sensor('mtxrHlProcessorTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self.get_system_sensor('mtxrHlSensorTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self.get_system_sensor('mtxrHlTemperature', Sensor.UNIT_CELSIUS, 1))
        return result

    def get_other_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('mtxrHlProcessorFrequency', Sensor.UNIT_HERTZ, scale=Sensor.SCALE_MEGA))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
