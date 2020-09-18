from nav.mibs import reduce_index
from nav.mibs.dlink import DLink
from nav.models.manage import Sensor
import inspect


class DLink_DGS_1210_XX(DLink):

    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        columns = yield reduce_index(self.retrieve_columns([
            'ddmStatusPort',
            'ddmRxPower',
            'ddmTxPower',
            'ddmVoltage',
            'ddmTemperature',
            'ddmBiasCurrent'
        ]))
        result = []
        for _, item in columns.items():
            port = item.get('ddmStatusPort')
            result.append(self.get_port_sensor(port, 'ddmRxPower', Sensor.UNIT_DBM))
            result.append(self.get_port_sensor(port, 'ddmTxPower', Sensor.UNIT_DBM))
            result.append(self.get_port_sensor(port, 'ddmVoltage', Sensor.UNIT_VOLTS_DC))
            result.append(self.get_port_sensor(port, 'ddmTemperature', Sensor.UNIT_CELSIUS))
            result.append(self.get_port_sensor(port, 'ddmBiasCurrent', Sensor.UNIT_AMPERES, Sensor.SCALE_MILLI))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
