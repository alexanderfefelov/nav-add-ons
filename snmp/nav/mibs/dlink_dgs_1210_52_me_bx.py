from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer


class DLink_DGS_1210_52_ME_BX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_52ME_BX_7_02_017_mib')
    ROOT_OID = 'dgs-1210-52mebx'
    GET_DDM_SENSORS = 'get_ddm_sensors'
    GET_FAN_SENSORS = '_get_fan_sensors'
    GET_TEMPERATURE_SENSORS = '_get_temperature_sensors'

    @defer.inlineCallbacks
    def _get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        is_supported = yield self.is_oid_supported(self.ROOT_OID)
        if is_supported:
            result.append(self.get_system_sensor('sysSmartFanStatus', ''))
        else:
            self._logger.warning('%s is not supported', self.ROOT_OID)
        defer.returnValue(result)

    @defer.inlineCallbacks
    def _get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        is_supported = yield self.is_oid_supported(self.ROOT_OID)
        if is_supported:
            result.append(self.get_system_sensor('sysTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
        else:
            self._logger.warning('%s is not supported', self.ROOT_OID)
        defer.returnValue(result)


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
