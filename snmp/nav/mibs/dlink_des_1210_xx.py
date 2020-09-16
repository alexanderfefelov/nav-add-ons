import inspect
from nav.mibs import reduce_index
from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from twisted.internet import defer


class _DLink_DES_1210_XX_Mib(MibRetriever):

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        system_poe_sensors = yield self._get_system_poe_sensors()
        result = []
        result.extend(system_poe_sensors)
        defer.returnValue(result)

    def _get_system_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self._get_sensor('pethPsePortPowerBudget', Sensor.UNIT_WATTS))
        result.append(self._get_sensor('pethPsePortPowerConsumption', Sensor.UNIT_WATTS))
        result.append(self._get_sensor('pethPsePortPowerRemainder', Sensor.UNIT_WATTS))
        result.append(self._get_sensor('pethPsePortPowerRatioOfSystemPower', Sensor.UNIT_PERCENT))
        return result

    def _get_sensor(self, sensor, unit_of_measurement):
        self._logger.debug(here(self))
        module_name = self.get_module_name()
        oid = str(self.nodes[sensor].oid) + '.0'
        internal_name = sensor
        description = internal_name
        return dict(
            mib=module_name,
            oid=oid,
            name=internal_name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=0,
            scale=None
        )


here = lambda this : '{}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
