from nav.mibs.dlink_des_1210_xx import DLink_DES_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_DES_1210_28_P_CX_Mib(MibRetriever, DLink_DES_1210_XX):
    mib = get_mib('D_Link_DES_1210_28P_CX_4_12_004_mib')
    GUARD_OID = 'des-1210-28p-cx'
    GET_PORTS_POE_SENSORS = 'get_ports_poe_sensors'
    GET_SYSTEM_POE_SENSORS = 'get_system_poe_sensors'
