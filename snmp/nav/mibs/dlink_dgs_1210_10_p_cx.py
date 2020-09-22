from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_DGS_1210_10_P_CX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_10P_CX_4_10_002_mib')
    ROOT_OID = 'dgs-1210-10pcx'
    GET_PORTS_POE_SENSORS = 'ports_poe_sensors'
    GET_SYSTEM_POE_SENSORS = 'system_poe_sensors'
