from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.smidumps import get_mib
from nav.models.manage import Sensor
from twisted.internet import defer
import inspect


class TPLink_Poe_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('TP_Link_tplink_powerOverEthernet_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        ports_poe_sensors = yield self.get_ports_poe_sensors()
        result.extend(ports_poe_sensors)
        system_poe_sensors = yield self.get_system_poe_sensors()
        result.extend(system_poe_sensors)
        self._logger.info('%d sensor(s) detected', len(result))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_ports_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'tpPoePortIndex',
            'tpPoePower',
            'tpPoePowerLimit',
            'tpPoeVoltage',
            'tpPoeCurrent',
            'tpPoePowerStatus'
        ])
        if columns:
            for _, item in columns.items():
                port = item.get('tpPoePortIndex')
                result.append(self.get_port_sensor(port, 'tpPoePower', Sensor.UNIT_WATTS, precision=1))
                result.append(self.get_port_sensor(port, 'tpPoePowerLimit', Sensor.UNIT_WATTS, precision=1))
                result.append(self.get_port_sensor(port, 'tpPoeVoltage', Sensor.UNIT_VOLTS_DC, precision=1))
                result.append(self.get_port_sensor(port, 'tpPoeCurrent', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
                result.append(self.get_port_sensor(port, 'tpPoePowerStatus', ''))
        defer.returnValue(result)

    def get_system_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('tpSystemPowerLimit', Sensor.UNIT_WATTS, precision=1))
        result.append(self.get_system_sensor('tpSystemPowerConsumption', Sensor.UNIT_WATTS, precision=1))
        result.append(self.get_system_sensor('tpSystemPowerRemain', Sensor.UNIT_WATTS, precision=1))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
