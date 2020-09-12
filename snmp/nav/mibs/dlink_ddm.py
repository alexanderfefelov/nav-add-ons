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
            'swDdmPortState',
            'swDdmRxPower',
            'swDdmTxPower',
            'swDdmVoltage',
            'swDdmTemperature',
            'swDdmBiasCurrent',
        ])
        result.addCallback(reduce_index)
        return result

    def _get_ddm_sensors(self, data):
        result = []
        module_name = self.get_module_name()
        for _, item in data.items():
            if item.get('swDdmPortState', None) == 1:
                port = str(item.get('swDdmPort'))

                oid = str(self.nodes['swDdmRxPower'].oid) + port
                internal_name = 'swDdmRxPower.{}'.format(port)
                description = internal_name
                result.append(dict(
                    mib=module_name,
                    oid=oid,
                    name=internal_name,
                    internal_name=internal_name,
                    description=description,
                    unit_of_measurement=Sensor.UNIT_DBM,
                    precision=0,
                    scale=None
                ))

                oid = str(self.nodes['swDdmTxPower'].oid) + port
                internal_name = 'swDdmTxPower.{}'.format(port)
                description = internal_name
                result.append(dict(
                    mib=module_name,
                    oid=oid,
                    name=internal_name,
                    internal_name=internal_name,
                    description=description,
                    unit_of_measurement=Sensor.UNIT_DBM,
                    precision=0,
                    scale=None
                ))

                oid = str(self.nodes['swDdmVoltage'].oid) + port
                internal_name = 'swDdmVoltage.{}'.format(port)
                description = internal_name
                result.append(dict(
                    mib=module_name,
                    oid=oid,
                    name=internal_name,
                    internal_name=internal_name,
                    description=description,
                    unit_of_measurement=Sensor.UNIT_VOLTS_DC,
                    precision=0,
                    scale=None
                ))

                oid = str(self.nodes['swDdmTemperature'].oid) + port
                internal_name = 'swDdmTemperature.{}'.format(port)
                description = internal_name
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

                oid = str(self.nodes['swDdmBiasCurrent'].oid) + port
                internal_name = 'swDdmBiasCurrent.{}'.format(port)
                description = internal_name
                result.append(dict(
                    mib=module_name,
                    oid=oid,
                    name=internal_name,
                    internal_name=internal_name,
                    description=description,
                    unit_of_measurement=Sensor.UNIT_AMPERES,
                    precision=0,
                    scale=Sensor.SCALE_MILLI
                ))
        return result
