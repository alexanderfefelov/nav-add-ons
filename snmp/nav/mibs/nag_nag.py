from nav.mibs.mibretriever import MibRetriever
from nav.mibs.snmp_add_on import SnmpAddOn
from nav.models.manage import Sensor
from nav.smidumps import get_mib
from twisted.internet import defer
import inspect


class Nag_Nag_Mib(MibRetriever, SnmpAddOn):
    mib = get_mib('NAG_SNR_SWITCH_private_2_1_80_mib')

    @defer.inlineCallbacks
    def get_cpu_loadavg(self):
        self._logger.debug(here(self))
        result = {}
        for cpu in 'sys', 'switch':
            idle_30_sec = yield self.get_next(cpu + 'CPUThirtySecondIdle')
            if idle_30_sec:
                idle_5_min = yield self.get_next(cpu + 'CPUFiveMinuteIdle')
                load_30_sec = 100 - idle_30_sec
                load_5_min = 100 - idle_5_min
                result.update({
                    cpu: [
                        (1, load_30_sec),
                        (5, load_5_min)
                    ]
                })
        defer.returnValue(result)

    def get_cpu_utilization(self):
        self._logger.debug(here(self))
        return defer.succeed(None)

    @defer.inlineCallbacks
    def get_memory_usage(self):
        self._logger.debug(here(self))
        result = {}
        for pool in 'sys', 'switch':
            size = yield self.get_next(pool + 'MemorySize')
            if size:
                used = yield self.get_next(pool + 'MemoryBusy')
                free = size - used
                result.update({
                  pool: (used, free)
                })
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_all_sensors(self):
        self._logger.debug(here(self))
        result = []
        ddm_sensors = yield self.get_ddm_sensors()
        result.extend(ddm_sensors)
        fan_sensors = yield self.get_fan_sensors()
        result.extend(fan_sensors)
        ports_poe_sensors = yield self.get_ports_poe_sensors()
        result.extend(ports_poe_sensors)
        system_poe_sensors = yield self.get_system_poe_sensors()
        result.extend(system_poe_sensors)
        temperature_sensors = yield self.get_temperature_sensors()
        result.extend(temperature_sensors)
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_ddm_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'ddmDiagnosisIfIndex',
            'ddmDiagnosisTemperature',
            'ddmDiagnosisVoltage',
            'ddmDiagnosisBias',
            'ddmDiagnosisRXPower',
            'ddmDiagnosisTXPower'
        ])
        if columns:
            for _, item in columns.items():
                port = item.get('ddmDiagnosisIfIndex')
                result.append(self.get_port_sensor(port, 'ddmDiagnosisRXPower', Sensor.UNIT_DBM))
                result.append(self.get_port_sensor(port, 'ddmDiagnosisTXPower', Sensor.UNIT_DBM))
                result.append(self.get_port_sensor(port, 'ddmDiagnosisVoltage', Sensor.UNIT_VOLTS_DC))
                result.append(self.get_port_sensor(port, 'ddmDiagnosisTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
                result.append(self.get_port_sensor(port, 'ddmDiagnosisBias', Sensor.UNIT_AMPERES, scale=Sensor.SCALE_MILLI))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_fan_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'sysFanIndex',
            'sysFanStatus',
            'sysFanSpeed'
        ])
        if columns:
            for _, item in columns.items():
                index = item.get('sysFanIndex')
                result.append(self.get_indexed_system_sensor(index, 'sysFanStatus', ''))
                result.append(self.get_indexed_system_sensor(index, 'sysFanSpeed', Sensor.UNIT_RPM))
        defer.returnValue(result)

    @defer.inlineCallbacks
    def get_ports_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        columns = yield self.retrieve_columns([
            'poePortIndex',
            'poePortMaxPower',
            'poePortCurrentPower',
            'poePortCurrentCurrent',
            'poePortCurrentVoltage'
        ])
        if columns:
            for _, item in columns.items():
                port = item.get('poePortIndex')
                result.append(self.get_port_sensor(port, 'poePortMaxPower', Sensor.UNIT_WATTS))
                result.append(self.get_port_sensor(port, 'poePortCurrentPower', Sensor.UNIT_WATTS))
                result.append(self.get_port_sensor(port, 'poePortCurrentCurrent', Sensor.UNIT_AMPERES))
                result.append(self.get_port_sensor(port, 'poePortCurrentVoltage', Sensor.UNIT_VOLTS_DC))
        defer.returnValue(result)

    def get_system_poe_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('poeMaxPower', Sensor.UNIT_WATTS))
        result.append(self.get_system_sensor('poeCurrentPower', Sensor.UNIT_WATTS))
        return result

    def get_temperature_sensors(self):
        self._logger.debug(here(self))
        result = []
        result.append(self.get_system_sensor('sysTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
        result.append(self.get_system_sensor('switchTemperature', Sensor.UNIT_CELSIUS, minimum=-20, maximum=120))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
