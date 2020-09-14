from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer


class MikroTikMikrotikMib(MibRetriever):
    mib = get_mib('MikroTik_mikrotik_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        fans = yield self._get_fan_sensors()
        other = yield self._get_other_sensors()
        power_supply = yield self._get_power_supply_sensors()
        temperatures = yield self._get_temperature_sensors()
        defer.returnValue(fans + other + power_supply + temperatures)

    def _get_sensor(self, sensor, unit_of_measurement, precision=0, scale=None):
        module_name = self.get_module_name()
        oid = str(self.nodes[sensor].oid) + '.0'
        internal_name = sensor
        description = internal_name
        return dict(
            mib=module_name,
            oid=oid,
            name=internal_name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale
        )

    def _get_fan_sensors(self):
        result = []
        result.append(self._get_sensor('mtxrHlActiveFan', ''))
        result.append(self._get_sensor('mtxrHlFanSpeed1', Sensor.UNIT_RPM))
        result.append(self._get_sensor('mtxrHlFanSpeed2', Sensor.UNIT_RPM))
        return result

    def _get_other_sensors(self):
        result = []
        result.append(self._get_sensor('mtxrHlProcessorFrequency', Sensor.UNIT_HERTZ, scale=Sensor.SCALE_MEGA))
        return result

    def _get_power_supply_sensors(self):
        result = []
        result.append(self._get_sensor('mtxrHlBackupPowerSupplyState', ''))
        result.append(self._get_sensor('mtxrHlPowerSupplyState', ''))
        result.append(self._get_sensor('mtxrHlCurrent', Sensor.UNIT_AMPERES, 3))
        result.append(self._get_sensor('mtxrHlPower', Sensor.UNIT_WATTS, 1))
        result.append(self._get_sensor('mtxrHlCoreVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self._get_sensor('mtxrHlFiveVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self._get_sensor('mtxrHlThreeDotThreeVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self._get_sensor('mtxrHlTwelveVoltage', Sensor.UNIT_VOLTS_DC))
        result.append(self._get_sensor('mtxrHlVoltage', Sensor.UNIT_VOLTS_AC))
        return result

    def _get_temperature_sensors(self):
        result = []
        result.append(self._get_sensor('mtxrHlBoardTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self._get_sensor('mtxrHlCpuTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self._get_sensor('mtxrHlProcessorTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self._get_sensor('mtxrHlSensorTemperature', Sensor.UNIT_CELSIUS, 1))
        result.append(self._get_sensor('mtxrHlTemperature', Sensor.UNIT_CELSIUS, 1))
        return result
