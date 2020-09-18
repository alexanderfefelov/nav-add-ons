from nav.mibs import reduce_index
from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class DLink_Equipment_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('D_Link_Equipment_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        fan_sensors = yield self.get_fan_sensors()
        temperature_sensors = yield self.get_temperature_sensors()
        result.extend(fan_sensors)
        result.extend(temperature_sensors)
        self._logger.debug(str(result))
        defer.returnValue(result)

    def get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield reduce_index(self.retrieve_columns([
            'swFanUnitIndex',
            'swFanID',
            'swFanNumber',
            'swFanStatus',
            'swFanSpeed'
        ]))
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
        return result

    def get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield reduce_index(self.retrieve_columns([
            'swTemperatureUnitIndex',
            'swTemperatureCurrent'
        ]))
        for _, item in columns.items():
            index = item.get('swTemperatureUnitIndex')
            result.append(self.get_indexed_system_sensor(index, 'swTemperatureCurrent', Sensor.UNIT_CELSIUS))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
