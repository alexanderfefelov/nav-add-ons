from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from twisted.internet import defer
from twisted.internet.defer import returnValue
import inspect


class DLink(SnmpAddOn):
    SUPPORTED_ROOT = 'd-link'

    @defer.inlineCallbacks
    def is_supported(self):
        self._logger.debug(here(self))
        reply = yield self.get_next(self.SUPPORTED_ROOT)
        returnValue(bool(reply))

    @defer.inlineCallbacks
    def get_cpu_loadavg(self):
        self._logger.debug(here(self))
        utilization1 = yield self.get_next('agentCPUutilizationIn1min')
        utilization5 = yield self.get_next('agentCPUutilizationIn5min')
        if utilization1 or utilization5:
            result = dict(cpu=[
                (1, utilization1),
                (5, utilization5)
            ])
            defer.returnValue(result)

    def get_cpu_utilization(self):
        self._logger.debug(here(self))
        return defer.succeed(None)

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        ok = yield self.is_supported()
        if ok:
            ddm_sensors = yield self.get_ddm_sensors()
            fan_sensors = yield self.get_fan_sensors()
            ports_poe_sensors = yield self.get_ports_poe_sensors()
            system_poe_sensors = yield self.get_system_poe_sensors()
            temperature_sensors = yield self.get_temperature_sensors()
            result.extend(ddm_sensors)
            result.extend(fan_sensors)
            result.extend(ports_poe_sensors)
            result.extend(system_poe_sensors)
            result.extend(temperature_sensors)
        self._logger.debug(str(result))
        defer.returnValue(result)

    # Default sensors implementations are no sensors at all

    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        return []

    def get_fan_sensors(self):
        self._logger.debug(here(self))
        return []

    def get_ports_poe_sensors(self):
        self._logger.debug(here(self))
        return []

    def get_system_poe_sensors(self):
        self._logger.debug(here(self))
        return []

    def get_temperature_sensors(self):
        self._logger.debug(here(self))
        return []

    # Concrete sensors implementations

    @defer.inlineCallbacks
    def _get_ddm_sensors(self):
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
                result.append(self.get_port_sensor(port, 'ddmTemperature', Sensor.UNIT_CELSIUS))
                result.append(self.get_port_sensor(port, 'ddmBiasCurrent', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def _get_ddm_sensors_old(self):
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
                    result.append(self.get_port_sensor(port, 'swDdmTemperature', Sensor.UNIT_CELSIUS))
                    result.append(self.get_port_sensor(port, 'swDdmBiasCurrent', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def _get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'swFanUnitIndex',
            'swFanID',
            'swFanNumber',
            'swFanStatus',
            'swFanSpeed'
        ])
        if columns:
            module_name = self.get_module_name()
            for _, item in columns.items():
                unit_index = item.get('swFanUnitIndex')
                fan_id = item.get('swFanID')
                fan_number = item.get('swFanNumber')
                oid = str(self.nodes['swFanSpeed'].oid) + str(item.get(0, None))
                internal_name = 'swFanSpeed.{}/{}/{}'.format(str(unit_index), str(fan_id), str(fan_number))
                description = 'Fan {}/{}/{} work speed'.format(str(unit_index), str(fan_id), str(fan_number))
                result.append(dict(
                    mib=module_name,
                    oid=oid,
                    name=internal_name,
                    internal_name=internal_name,
                    description=description,
                    unit_of_measurement=Sensor.UNIT_RPM,
                    precision=0,
                    scale=None
                ))

                oid = str(self.nodes['swFanStatus'].oid) + str(item.get(0, None))
                internal_name = 'swFanStatus.{}/{}/{}'.format(str(unit_index), str(fan_id), str(fan_number))
                description = 'Fan {}/{}/{} status'.format(str(unit_index), str(fan_id), str(fan_number))
                result.append(dict(
                    mib=module_name,
                    oid=oid,
                    name=internal_name,
                    internal_name=internal_name,
                    description=description,
                    unit_of_measurement='',
                    precision=0,
                    scale=None
                ))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def _get_ports_poe_sensors(self):
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
    def _get_system_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('pethPsePortPowerBudget', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerConsumption', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerRemainder', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerRatioOfSystemPower', Sensor.UNIT_PERCENT))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def _get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'swTemperatureUnitIndex',
            'swTemperatureCurrent'
        ])
        if columns:
            for _, item in columns.items():
                index = item.get('swTemperatureUnitIndex')
                result.append(self.get_indexed_system_sensor(index, 'swTemperatureCurrent', Sensor.UNIT_CELSIUS))
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
