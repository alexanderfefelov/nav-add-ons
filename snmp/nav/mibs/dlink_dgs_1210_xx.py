from nav.mibs import reduce_index
from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from twisted.internet import defer


class _DLink_DGS_1210_XX_Mib(MibRetriever):

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

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        ddm_columns = yield self._get_ddm_columns()
        ddm_sensors = self._get_ddm_sensors(ddm_columns)
        result = []
        result.extend(ddm_sensors)
        defer.returnValue(result)

    def _get_ddm_columns(self):
        self._logger.debug(here(self))
        result = self.retrieve_columns([
            'ddmStatusPort',
            'ddmRxPower',
            'ddmTxPower',
            'ddmVoltage',
            'ddmTemperature',
            'ddmBiasCurrent'
        ])
        result.addCallback(reduce_index)
        return result

    def _get_ddm_sensors(self, data):
        self._logger.debug(here(self))
        result = []
        for _, item in data.items():
            port = item.get('ddmStatusPort')
            result.append(self._get_port_sensor(port, 'ddmRxPower', Sensor.UNIT_DBM))
            result.append(self._get_port_sensor(port, 'ddmTxPower', Sensor.UNIT_DBM))
            result.append(self._get_port_sensor(port, 'ddmVoltage', Sensor.UNIT_VOLTS_DC))
            result.append(self._get_port_sensor(port, 'ddmTemperature', Sensor.UNIT_CELSIUS))
            result.append(self._get_port_sensor(port, 'ddmBiasCurrent', Sensor.UNIT_AMPERES, Sensor.SCALE_MILLI))
        return result

    def _get_port_sensor(self, port, sensor, unit_of_measurement, scale=None):
        self._logger.debug(here(self))
        module_name = self.get_module_name()
        oid = str(self.nodes[sensor].oid) + '.' + str(port)
        internal_name = '{}.{}'.format(sensor, str(port))
        description = internal_name
        return dict(
            mib=module_name,
            oid=oid,
            ifindex=port,
            name=internal_name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=0,
            scale=scale
        )

here = lambda this : '{}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
