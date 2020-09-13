from nav.mibs import reduce_index
from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer


class DLinkDdmMib(MibRetriever):
    mib = get_mib('D_Link_DDM_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        ddm_columns = yield self._get_ddm_columns()
        ddm_sensors = self._get_ddm_sensors(ddm_columns)
        result = []
        result.extend(ddm_sensors)
        defer.returnValue(result)

    def _get_ddm_columns(self):
        result = self.retrieve_columns([
            'swDdmPort',
            'swDdmRxPower',
            'swDdmTxPower',
            'swDdmVoltage',
            'swDdmTemperature',
            'swDdmBiasCurrent'
        ])
        result.addCallback(reduce_index)
        return result

    def _get_ddm_sensors(self, data):
        result = []
        for _, item in data.items():
            port = item.get('swDdmPort')
            result.append(self._get_port_sensor(port, 'swDdmRxPower', Sensor.UNIT_DBM))
            result.append(self._get_port_sensor(port, 'swDdmTxPower', Sensor.UNIT_DBM))
            result.append(self._get_port_sensor(port, 'swDdmVoltage', Sensor.UNIT_VOLTS_DC))
            result.append(self._get_port_sensor(port, 'swDdmTemperature', Sensor.UNIT_CELSIUS))
            result.append(self._get_port_sensor(port, 'swDdmBiasCurrent', Sensor.UNIT_AMPERES, Sensor.SCALE_MILLI))
        return result

    def _get_port_sensor(self, port, sensor, unit_of_measurement, scale=None):
        module_name = self.get_module_name()
        oid = str(self.nodes[sensor].oid) + '.' + str(port)
        internal_name = '{}.{}'.format(sensor, str(port))
        description = internal_name
        return dict(
            mib=module_name,
            oid=oid,
            name=internal_name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=0,
            scale=scale
        )
