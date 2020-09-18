from nav.mibs import reduce_index
from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class Nag_Nag_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('NAG_SNR_SWITCH_private_2_1_80_mib')

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        ddm_sensors = yield self.get_ddm_sensors()
        result.extend(ddm_sensors)
        self._logger.debug(str(result))
        defer.returnValue(result)

    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        columns = yield reduce_index(self.retrieve_columns([
            'ddmDiagnosisIfIndex',
            'ddmDiagnosisTemperature',
            'ddmDiagnosisVoltage',
            'ddmDiagnosisBias',
            'ddmDiagnosisRXPower',
            'ddmDiagnosisTXPower'
        ]))
        result = []
        for _, item in columns.items():
            port = item.get('ddmDiagnosisIfIndex')
            result.append(self.get_port_sensor(port, 'ddmDiagnosisRXPower', Sensor.UNIT_DBM))
            result.append(self.get_port_sensor(port, 'ddmDiagnosisTXPower', Sensor.UNIT_DBM))
            result.append(self.get_port_sensor(port, 'ddmDiagnosisVoltage', Sensor.UNIT_VOLTS_DC))
            result.append(self.get_port_sensor(port, 'ddmDiagnosisTemperature', Sensor.UNIT_CELSIUS))
            result.append(self.get_port_sensor(port, 'ddmDiagnosisBias', Sensor.UNIT_AMPERES, Sensor.SCALE_MILLI))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
