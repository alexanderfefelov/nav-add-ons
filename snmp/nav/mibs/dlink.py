from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from twisted.internet import defer
import inspect


class DLink(SnmpAddOn):
    GET_DDM_SENSORS = 'empty'
    GET_FAN_SENSORS = 'empty'
    GET_PORTS_POE_SENSORS = 'empty'
    GET_POWER_SENSORS = 'empty'
    GET_SYSTEM_POE_SENSORS = 'empty'
    GET_TEMPERATURE_SENSORS = 'empty'

    @defer.inlineCallbacks
    def get_cpu_loadavg(self):
        self._logger.debug(here(self))
        result = {}
        utilization_1_min = yield self.get_next('agentCPUutilizationIn1min')
        if utilization_1_min:
            utilization_5_min = yield self.get_next('agentCPUutilizationIn5min')
            result['cpu'] = [
                (1, utilization_1_min),
                (5, utilization_5_min)
            ]
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_cpu_utilization(self):
        self._logger.debug(here(self))
        return defer.succeed(None)

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        ddm_sensors = yield getattr(self, self.GET_DDM_SENSORS)()
        result.extend(ddm_sensors)
        fan_sensors = yield getattr(self, self.GET_FAN_SENSORS)()
        result.extend(fan_sensors)
        ports_poe_sensors = yield getattr(self, self.GET_PORTS_POE_SENSORS)()
        result.extend(ports_poe_sensors)
        power_sensors = yield getattr(self, self.GET_POWER_SENSORS)()
        result.extend(power_sensors)
        system_poe_sensors = yield getattr(self, self.GET_SYSTEM_POE_SENSORS)()
        result.extend(system_poe_sensors)
        temperature_sensors = yield getattr(self, self.GET_TEMPERATURE_SENSORS)()
        result.extend(temperature_sensors)
        self._logger.info('%d sensor(s) detected', len(result))
        defer.returnValue(result)

    def empty(self):
        self._logger.debug(here(self))
        return []

    @defer.inlineCallbacks
    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'ddmStatusPort',
            'ddmRxPower',
            'ddmTxPower',
            'ddmVoltage',
            'ddmTemperature',
            'ddmBiasCurrent'
        ])
        if columns:
            for _, item in columns.items():
                port = item.get('ddmStatusPort')
                result.append(self.get_port_sensor(port, 'ddmRxPower', Sensor.UNIT_DBM))
                result.append(self.get_port_sensor(port, 'ddmTxPower', Sensor.UNIT_DBM))
                result.append(self.get_port_sensor(port, 'ddmVoltage', Sensor.UNIT_VOLTS_DC))
                result.append(self.get_port_sensor(port, 'ddmTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
                result.append(self.get_port_sensor(port, 'ddmBiasCurrent', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_ddm_sensors_old(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'swDdmPortState',
            'swDdmPort',
            'swDdmRxPower',
            'swDdmTxPower',
            'swDdmVoltage',
            'swDdmTemperature',
            'swDdmBiasCurrent'
        ])
        if columns:
            for _, item in columns.items():
                if item.get('swDdmPortState', None) == 1:
                    port = item.get('swDdmPort')
                    result.append(self.get_port_sensor(port, 'swDdmRxPower', Sensor.UNIT_DBM))
                    result.append(self.get_port_sensor(port, 'swDdmTxPower', Sensor.UNIT_DBM))
                    result.append(self.get_port_sensor(port, 'swDdmVoltage', Sensor.UNIT_VOLTS_DC))
                    result.append(self.get_port_sensor(port, 'swDdmTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
                    result.append(self.get_port_sensor(port, 'swDdmBiasCurrent', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_fan_sensors_old(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'swFanUnitIndex',
            'swFanID',
            'swFanStatus',
            'swFanSpeed'
        ])
        if columns:
            for _, item in columns.items():
                unit_index = item.get('swFanUnitIndex')
                fan_id = item.get('swFanID')
                self.get_double_indexed_system_sensor(unit_index, fan_id, 'swFanStatus', '')
                self.get_double_indexed_system_sensor(unit_index, fan_id, 'swFanSpeed', Sensor.UNIT_RPM)
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_ports_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'poeportgroup',
            'poeportid',
            'poePortPower',
            'poePortVoltage',
            'poePortCurrent'
        ])
        if columns:
            for _, item in columns.items():
                group = item.get('poeportgroup')
                port = item.get('poeportid')
                result.append(self.get_grouped_port_sensor(group, port, 'poePortPower', Sensor.UNIT_WATTS))
                result.append(self.get_grouped_port_sensor(group, port, 'poePortVoltage', Sensor.UNIT_VOLTS_DC))
                result.append(self.get_grouped_port_sensor(group, port, 'poePortCurrent', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_power_sensors_old(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'swPowerUnitIndex',
            'swPowerID',
            'swPowerStatus'
        ])
        if columns:
            for _, item in columns.items():
                unit_index = item.get('swPowerUnitIndex')
                power_id = item.get('swPowerID')
                self.get_double_indexed_system_sensor(unit_index, power_id, 'swPowerStatus', '')
        defer.returnValue(result)

    def get_system_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('pethPsePortPowerBudget', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerConsumption', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerRemainder', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerRatioOfSystemPower', Sensor.UNIT_PERCENT))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_temperature_sensors_old(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'swTemperatureUnitIndex',
            'swTemperatureCurrent'
        ])
        if columns:
            for _, item in columns.items():
                index = item.get('swTemperatureUnitIndex')
                result.append(self.get_indexed_system_sensor(index, 'swTemperatureCurrent', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
