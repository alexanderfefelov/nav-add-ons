from nav.mibs.mibretriever import MibRetriever
from nav.mibs.dlink import DLink
from nav.smidumps import get_mib


class DLink_Equipment_Mib(MibRetriever, DLink):
    mib = get_mib('D_Link_Equipment_mib')
    ROOT_OID = 'swEquipmentMIB'
    GET_FAN_SENSORS = '_get_fan_sensors_old'
    GET_POWER_SENSORS = '_get_power_sensors_old'
    GET_TEMPERATURE_SENSORS = '_get_temperature_sensors_old'
