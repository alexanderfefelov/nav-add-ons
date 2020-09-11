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
        for idx, obj in data.items():
            if obj.get('swDdmPortState', None) == 1:
                port = obj.get('swDdmPort')

                oid = str(self.nodes['swDdmRxPower'].oid) + str(obj.get(0, None))
                internal_name = 'swDdmRxPower.{}'.format(str(port))
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

                oid = str(self.nodes['swDdmTxPower'].oid) + str(obj.get(0, None))
                internal_name = 'swDdmTxPower.{}'.format(str(port))
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

                oid = str(self.nodes['swDdmVoltage'].oid) + str(obj.get(0, None))
                internal_name = 'swDdmVoltage.{}'.format(str(port))
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

                oid = str(self.nodes['swDdmTemperature'].oid) + str(obj.get(0, None))
                internal_name = 'swDdmTemperature.{}'.format(str(port))
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

                oid = str(self.nodes['swDdmBiasCurrent'].oid) + str(obj.get(0, None))
                internal_name = 'swDdmBiasCurrent.{}'.format(str(port))
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
