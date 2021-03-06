from nav.mibs.dlink_des_1210_xx import DLink_DES_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_DES_1210_08_P_BX_Mib(MibRetriever, DLink_DES_1210_XX):
    mib = get_mib('D_Link_DES_1210_08P_BX_v3_12_004_mib')
    GET_PORTS_POE_SENSORS = 'get_ports_poe_sensors'
    GET_SYSTEM_POE_SENSORS = 'get_system_poe_sensors'
