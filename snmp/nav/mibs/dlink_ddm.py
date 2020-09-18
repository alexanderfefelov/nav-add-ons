from nav.mibs import reduce_index
from nav.mibs.dlink import DLink
from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class DLink_Ddm_Mib(MibRetriever, DLink):
    mib = get_mib('D_Link_DDM_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        ddm_sensors = yield self._get_ddm_sensors()
        result.extend(ddm_sensors)
        self._logger.debug(str(result))
        defer.returnValue(result)

    def _get_ddm_sensors(self):
        self._logger.debug(here(self))
        columns = yield reduce_index(self.retrieve_columns([
            'swDdmPort',
            'swDdmRxPower',
            'swDdmTxPower',
            'swDdmVoltage',
            'swDdmTemperature',
            'swDdmBiasCurrent'
        ]))
        result = []
        for _, item in columns.items():
            port = item.get('swDdmPort')
            result.append(self.get_port_sensor(port, 'swDdmRxPower', Sensor.UNIT_DBM))
            result.append(self.get_port_sensor(port, 'swDdmTxPower', Sensor.UNIT_DBM))
            result.append(self.get_port_sensor(port, 'swDdmVoltage', Sensor.UNIT_VOLTS_DC))
            result.append(self.get_port_sensor(port, 'swDdmTemperature', Sensor.UNIT_CELSIUS))
            result.append(self.get_port_sensor(port, 'swDdmBiasCurrent', Sensor.UNIT_AMPERES, Sensor.SCALE_MILLI))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
