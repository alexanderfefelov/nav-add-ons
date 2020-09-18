from nav.mibs import reduce_index
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from twisted.internet import defer
import inspect


class DLink(SnmpAddOn):

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

    def get_ports_poe_sensors(self):
        self._logger.debug(here(self))
        columns = yield reduce_index(self.retrieve_columns([
            'poeportgroup',
            'poeportid',
            'poePortPower',
            'poePortVoltage',
            'poePortCurrent'
        ]))
        result = []
        for _, item in columns.items():
            group = item.get('poeportgroup')
            port = item.get('poeportid')
            result.append(self.get_grouped_port_sensor(group, port, 'poePortPower', Sensor.UNIT_WATTS))
            result.append(self.get_grouped_port_sensor(group, port, 'poePortVoltage', Sensor.UNIT_VOLTS_DC))
            result.append(self.get_grouped_port_sensor(group, port, 'poePortCurrent', Sensor.UNIT_AMPERES, Sensor.SCALE_MILLI))
        return result

    def get_system_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('pethPsePortPowerBudget', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerConsumption', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerRemainder', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('pethPsePortPowerRatioOfSystemPower', Sensor.UNIT_PERCENT))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
