from twisted.internet import defer
from nav.mibs import reduce_index
from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from nav.smidumps import get_mib


class DLinkEquipmentMib(MibRetriever):

    mib = get_mib('D_Link_Equipment_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        fan_columns = yield self._get_fan_columns()
        fan_sensors = self._get_fan_sensors(fan_columns)
        temperature_columns = yield self._get_temperature_columns()
        temperature_sensors = self._get_temperature_sensors(temperature_columns)
        result = []
        result.extend(fan_sensors)
        result.extend(temperature_sensors)
        defer.returnValue(result)

    def _get_fan_columns(self):
        result = self.retrieve_columns([
            'swFanUnitIndex',
            'swFanID',
            'swFanNumber',
            'swFanSpeed'
        ])
        result.addCallback(reduce_index)
        return result

    def _get_fan_sensors(self, data):
        result = []
        for idx, obj in data.items():
            unit_index = obj.get('swFanUnitIndex')
            fan_id = obj.get('swFanID')
            fan_number = obj.get('swFanNumber')

            module_name = self.get_module_name()
            oid = str(self.nodes['swFanSpeed'].oid) + str(obj.get(0, None))
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
        return result

    def _get_temperature_columns(self):
        result = self.retrieve_columns([
            'swTemperatureUnitIndex',
            'swTemperatureCurrent'
        ])
        result.addCallback(reduce_index)
        return result

    def _get_temperature_sensors(self, data):
        result = []
        for idx, obj in data.items():
            unit_index = obj.get('swTemperatureUnitIndex')

            module_name = self.get_module_name()
            oid = str(self.nodes['swTemperatureCurrent'].oid) + str(obj.get(0, None))
            internal_name = 'swTemperatureCurrent.{}'.format(str(unit_index))
            description = 'Temperature {}'.format(str(unit_index))
            result.append(dict(
                mib=module_name,
                oid=oid,
                name=internal_name,
                internal_name=internal_name,
                description=description,
                unit_of_measurement=Sensor.UNIT_CELSIUS,
                precision=0,
                scale=None
            ))
        return result
